#!/usr/bin/env python3
"""Migrate KB subfolders into Logseq journals via the MCP HTTP server.

Usage:
    python3 migrate_kb_to_logseq.py                 # push everything
    python3 migrate_kb_to_logseq.py --dry-run       # scan + convert, no writes
    python3 migrate_kb_to_logseq.py --folders AI,Math
    python3 migrate_kb_to_logseq.py --only-existing # report sizes of existing pages

Requires: requests, tqdm  (pip install requests tqdm)
"""

import argparse
import json
import os
import re
import subprocess
import sys
import time
from collections import defaultdict
from datetime import datetime
from pathlib import Path

try:
    import requests
except ImportError:
    sys.exit("Missing dependency: requests. Install with `pip install requests`.")

try:
    from tqdm import tqdm
except ImportError:
    sys.exit("Missing dependency: tqdm. Install with `pip install tqdm`.")


# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

CONTENT_ROOT = Path(__file__).resolve().parent
KB_ROOT = CONTENT_ROOT / "KB"

FOLDERS = [
    "AI",
    "Jobs",
    "Language",
    "Math",
    "Medical",
    "Physics",
    "Parallel computing",
    "Robotics",
    "Software",
    "User Models",
    "Visualization",
]

MCP_URL = "http://127.0.0.1:12315/api"
MCP_TOKEN = "h6u7rp3m7"
HTTP_TIMEOUT = 10  # seconds per HTTP call
HTTP_RETRIES = 2  # retries on timeout
LARGE_PAGE_THRESHOLD = 25_000  # chars; above this, chunk + append

SKIP_FILENAMES = {".DS_Store", ".pages"}
SKIP_SUFFIXES = (".txt", ".ipynb", ".sh", ".pdf")
SKIP_NAME_PREFIXES = ("index", "__Index", "_Index_of_", ".")

MONTHS = [
    "jan",
    "feb",
    "mar",
    "apr",
    "may",
    "jun",
    "jul",
    "aug",
    "sep",
    "oct",
    "nov",
    "dec",
]
FULL_MONTHS = [
    "january",
    "february",
    "march",
    "april",
    "may",
    "june",
    "july",
    "august",
    "september",
    "october",
    "november",
    "december",
]
MONTH_LOOKUP = {m: i + 1 for i, m in enumerate(MONTHS)}
MONTH_LOOKUP.update({m: i + 1 for i, m in enumerate(FULL_MONTHS)})


# ---------------------------------------------------------------------------
# Date helpers
# ---------------------------------------------------------------------------


def ordinal(n: int) -> str:
    if 11 <= n <= 13:
        return "th"
    return {1: "st", 2: "nd", 3: "rd"}.get(n % 10, "th")


def to_logseq_date(y: int, m: int, d: int) -> str:
    return f"{MONTHS[m - 1]} {d}{ordinal(d)}, {y}"


def parse_date_string(s: str):
    """Try to parse various date formats. Returns (y, m, d) or None."""
    s = (s or "").strip().rstrip(",")
    if not s:
        return None
    # "Thursday 19th September 2024" / "Monday, October 10th 2022, 2:02:17 pm"
    m = re.match(r"\w+[,]?\s+(\d{1,2})(?:st|nd|rd|th)?\s+(\w+)\s+(\d{4})", s)
    if m:
        d, month_name, y = int(m.group(1)), m.group(2).lower(), int(m.group(3))
        if month_name in MONTH_LOOKUP:
            return (y, MONTH_LOOKUP[month_name], d)
    # "13-07-2024" / "13/07/2024"
    m = re.match(r"(\d{1,2})[-/](\d{1,2})[-/](\d{4})", s)
    if m:
        return (int(m.group(3)), int(m.group(2)), int(m.group(1)))
    # "2024-07-08"
    m = re.match(r"(\d{4})[-/](\d{1,2})[-/](\d{1,2})", s)
    if m:
        return (int(m.group(1)), int(m.group(2)), int(m.group(3)))
    return None


def git_first_commit_date(path: Path):
    """Returns (y, m, d) or None."""
    try:
        rel = path.relative_to(CONTENT_ROOT)
    except ValueError:
        return None
    try:
        out = (
            subprocess.run(
                [
                    "git",
                    "log",
                    "--diff-filter=A",
                    "--follow",
                    "--format=%ad",
                    "--date=short",
                    "--",
                    str(rel),
                ],
                cwd=CONTENT_ROOT,
                capture_output=True,
                text=True,
                timeout=5,
            )
            .stdout.strip()
            .split("\n")
        )
        if out and out[0]:
            y, m, d = out[0].split("-")
            return (int(y), int(m), int(d))
    except Exception:
        pass
    return None


def resolve_journal_date(path: Path, fm: dict) -> str:
    for key in ("date created", "date modified", "date"):
        if key in fm:
            parsed = parse_date_string(fm[key])
            if parsed:
                return to_logseq_date(*parsed)
    parsed = git_first_commit_date(path)
    if parsed:
        return to_logseq_date(*parsed)
    mt = datetime.fromtimestamp(path.stat().st_mtime)
    return to_logseq_date(mt.year, mt.month, mt.day)


# ---------------------------------------------------------------------------
# Frontmatter / conversion
# ---------------------------------------------------------------------------


def extract_frontmatter(text: str):
    """Returns (frontmatter_dict, body)."""
    if not text.startswith("---\n"):
        return {}, text
    end = text.find("\n---\n", 4)
    if end == -1:
        return {}, text
    fm_text = text[4:end]
    body = text[end + 5 :]
    fm = {}
    for line in fm_text.split("\n"):
        if ":" in line:
            k, _, v = line.partition(":")
            fm[k.strip()] = v.strip()
    return fm, body


def is_template_only(body: str, stem: str) -> bool:
    no_tpl = re.sub(r"<%[^>]*%>", "", body)
    no_toc = re.sub(r"```toc\s*```", "", no_tpl)
    no_heading = re.sub(
        r"^#\s*" + re.escape(stem) + r"\s*$", "", no_toc, flags=re.MULTILINE
    )
    no_heading = re.sub(r"^#\s*<%[^>]*%>\s*$", "", no_heading, flags=re.MULTILINE)
    return no_heading.strip() == ""


def convert_wiki_links(text: str) -> str:
    text = re.sub(r"\[\[([^\]|]+?)\.md\|([^\]]+?)\]\]", r"[[\2]]", text)
    text = re.sub(r"\[\[([^\]|]+?)\.md\]\]", r"[[\1]]", text)
    return text


def convert_images(text: str) -> str:
    text = re.sub(
        r"!\[\[[^\]]*?/?([^/\]|]+?\.(?:png|jpg|jpeg|gif|svg|webp))(?:\|[^\]]*)?\]\]",
        r"![[\1]]",
        text,
        flags=re.IGNORECASE,
    )
    text = re.sub(
        r"!\[[^\]]*\]\([^)]*?/?([^/)\]]+\.(?:png|jpg|jpeg|gif|svg|webp))\)",
        r"![[\1]]",
        text,
        flags=re.IGNORECASE,
    )
    return text


def should_skip(path: Path) -> bool:
    name = path.name
    if name in SKIP_FILENAMES:
        return True
    if name.lower().endswith(SKIP_SUFFIXES):
        return True
    for pref in SKIP_NAME_PREFIXES:
        if name.startswith(pref):
            return True
    return False


def convert_file(path: Path):
    """Returns (journal_name, content) or None if skipped."""
    if should_skip(path):
        return None
    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        text = path.read_text(encoding="utf-8", errors="replace")
    fm, body = extract_frontmatter(text)
    if is_template_only(body, path.stem):
        return None
    body = re.sub(r"^```toc\s*```\s*", "", body)
    body = convert_wiki_links(body)
    body = convert_images(body)
    body = body.strip()
    if not body:
        return None
    journal_name = resolve_journal_date(path, fm)
    try:
        rel = path.relative_to(CONTENT_ROOT)
    except ValueError:
        rel = path
    content = f"Source: `{rel}`\n\n{body}\n"
    return journal_name, content


# ---------------------------------------------------------------------------
# MCP HTTP client
# ---------------------------------------------------------------------------


class MCPClient:
    """Calls Logseq's native HTTP API directly (same endpoint the mcp-logseq
    package wraps). Endpoint: POST /api with JSON body {method, args}."""

    def __init__(self, url: str, token: str):
        self.url = url
        self.headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
        }

    def _post(self, method: str, args: list):
        """Returns (success, result_or_error)."""
        last_err = None
        for attempt in range(HTTP_RETRIES + 1):
            try:
                resp = requests.post(
                    self.url,
                    headers=self.headers,
                    json={"method": method, "args": args},
                    timeout=HTTP_TIMEOUT,
                )
                if resp.status_code == 401:
                    return (False, "401 Unauthorized — check MCP_TOKEN")
                if resp.status_code >= 400:
                    return (False, f"HTTP {resp.status_code}: {resp.text[:300]}")
                data = resp.json()
                # Logseq API returns {"error": ...} on failure
                if isinstance(data, dict) and "error" in data and data.get("error"):
                    return (False, str(data["error"]))
                return (True, data)
            except (requests.Timeout, requests.ConnectionError) as e:
                last_err = str(e)
                if attempt < HTTP_RETRIES:
                    time.sleep(0.5)
                    continue
        return (False, f"Network error after {HTTP_RETRIES + 1} attempts: {last_err}")

    def page_exists(self, page_name: str) -> bool:
        ok, result = self._post("logseq.Editor.getPage", [page_name])
        # getPage returns null/error when the page doesn't exist
        return (
            ok
            and result is not None
            and not (isinstance(result, dict) and result.get("name") is None)
        )

    def create_page(self, title: str, content: str):
        # Step 1: create the page with no first-block content
        ok, result = self._post(
            "logseq.Editor.createPage",
            [title, {}, {"createFirstBlock": True}],
        )
        if not ok:
            # Match the "already exists" wording the higher-level code expects
            if "exists" in str(result).lower() or "duplicate" in str(result).lower():
                return (False, "Page already exists")
            return (False, result)
        # Step 2: append the real content
        if content and content.strip():
            ok2, result2 = self._post(
                "logseq.Editor.appendBlockInPage",
                [title, content],
            )
            if not ok2:
                return (False, f"created but append failed: {result2}")
        return (True, result)

    def append_page(self, page_name: str, content: str):
        return self._post("logseq.Editor.appendBlockInPage", [page_name, content])

    def list_pages(self):
        return self._post("logseq.Editor.getAllPages", [])


# ---------------------------------------------------------------------------
# Pipeline
# ---------------------------------------------------------------------------


def scan_folder(folder_name: str):
    """Walk a KB subfolder and return list of (journal_name, content, source_path)."""
    root = KB_ROOT / folder_name
    if not root.exists():
        print(f"[warn] folder not found: {root}", file=sys.stderr)
        return []
    results = []
    files = sorted(p for p in root.rglob("*") if p.is_file())
    for path in tqdm(files, desc=f"scan {folder_name}", unit="file", leave=False):
        converted = convert_file(path)
        if converted is None:
            continue
        journal_name, content = converted
        results.append((journal_name, content, path))
    return results


def group_by_date(records):
    grouped = defaultdict(list)
    for journal_name, content, path in records:
        grouped[journal_name].append((content, path))
    return grouped


def combine_contents(items):
    """items: list of (content, path). Returns combined markdown."""
    if len(items) == 1:
        return items[0][0]
    return "\n\n---\n\n".join(content for content, _ in items)


def split_for_chunks(combined: str):
    """Split a large combined page into chunks under LARGE_PAGE_THRESHOLD."""
    parts = combined.split("\n\n---\n\n")
    chunks = []
    current = ""
    for i, part in enumerate(parts):
        sep = "\n\n---\n\n" if current else ""
        candidate = current + sep + part
        if len(candidate) > LARGE_PAGE_THRESHOLD and current:
            chunks.append(current)
            current = part
        else:
            current = candidate
    if current:
        chunks.append(current)
    return chunks


def push_journal(client: MCPClient, journal_name: str, combined: str, dry_run: bool):
    """Returns one of: 'created', 'skipped_existing', 'error:<msg>'."""
    if dry_run:
        return "would_create"
    if client.page_exists(journal_name):
        return "skipped_existing"

    if len(combined) <= LARGE_PAGE_THRESHOLD:
        ok, result = client.create_page(journal_name, combined)
        if ok:
            return "created"
        if "already exists" in str(result).lower():
            return "skipped_existing"
        return f"error:{result}"

    # Large page: create with first chunk, append the rest.
    chunks = split_for_chunks(combined)
    ok, result = client.create_page(journal_name, chunks[0])
    if not ok:
        if "already exists" in str(result).lower():
            return "skipped_existing"
        return f"error:{result}"
    for chunk in chunks[1:]:
        # Prepend separator so articles remain visually divided across chunks
        ok, result = client.append_page(journal_name, "\n\n---\n\n" + chunk)
        if not ok:
            return f"error:{result}"
    return "created"


def report_existing_only(client: MCPClient, grouped):
    """For --only-existing mode: list which target dates already exist."""
    print(f"Checking {len(grouped)} target journal dates...", file=sys.stderr)
    for journal_name in tqdm(sorted(grouped.keys()), desc="check", unit="date"):
        exists = client.page_exists(journal_name)
        n_files = len(grouped[journal_name])
        total_chars = sum(len(c) for c, _ in grouped[journal_name])
        flag = "EXISTS" if exists else "missing"
        print(
            f"  [{flag}] {journal_name}  ({n_files} files, {total_chars} chars)",
            file=sys.stderr,
        )


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------


def main():
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    ap.add_argument(
        "--dry-run", action="store_true", help="Scan and convert, but don't call MCP."
    )
    ap.add_argument(
        "--folders",
        type=str,
        default=None,
        help=f"Comma-separated subset of folders. Default: all of {','.join(FOLDERS)}",
    )
    ap.add_argument(
        "--only-existing",
        action="store_true",
        help="Check which target journal pages already exist; no writes.",
    )
    args = ap.parse_args()

    folders = args.folders.split(",") if args.folders else FOLDERS
    for f in folders:
        if f not in FOLDERS:
            sys.exit(f"Unknown folder: {f}. Valid: {', '.join(FOLDERS)}")

    if not KB_ROOT.exists():
        sys.exit(f"KB root not found: {KB_ROOT}")

    if args.dry_run:
        print("[dry-run] no MCP calls will be made", file=sys.stderr)
        client = None
    else:
        client = MCPClient(MCP_URL, MCP_TOKEN)
        # sanity ping
        ok, result = client.list_pages()
        if not ok:
            sys.exit(
                f"Cannot reach Logseq API at {MCP_URL}: {result}\n"
                f"Make sure Logseq is running with the HTTP API enabled."
            )

    start = time.time()
    totals = {
        "files_scanned": 0,
        "journals_created": 0,
        "journals_skipped": 0,
        "errors": 0,
    }
    all_grouped = {}

    for folder in folders:
        print(f"\n=== {folder} ===", file=sys.stderr)
        records = scan_folder(folder)
        grouped = group_by_date(records)
        all_grouped.update(grouped)
        totals["files_scanned"] += len(records)
        print(f"  {len(records)} files → {len(grouped)} unique dates", file=sys.stderr)

    if args.only_existing:
        report_existing_only(client, all_grouped)
        return

    print(f"\n--- Pushing {len(all_grouped)} journal pages ---", file=sys.stderr)
    for journal_name in tqdm(sorted(all_grouped.keys()), desc="push", unit="date"):
        combined = combine_contents(all_grouped[journal_name])
        status = push_journal(client, journal_name, combined, args.dry_run)
        if status == "created" or status == "would_create":
            totals["journals_created"] += 1
        elif status == "skipped_existing":
            totals["journals_skipped"] += 1
        else:
            totals["errors"] += 1
            print(f"  [error] {journal_name}: {status}", file=sys.stderr)

    elapsed = time.time() - start
    print(f"\n--- Done in {elapsed:.1f}s ---", file=sys.stderr)
    print(f"  Files scanned:       {totals['files_scanned']}", file=sys.stderr)
    label = "Journals to create " if args.dry_run else "Journals created   "
    print(f"  {label}:   {totals['journals_created']}", file=sys.stderr)
    print(
        f"  Journals skipped:    {totals['journals_skipped']} (already existed)",
        file=sys.stderr,
    )
    print(f"  Errors:              {totals['errors']}", file=sys.stderr)
    if args.dry_run:
        print(
            f"\n[dry-run] Re-run without --dry-run to push to Logseq.", file=sys.stderr
        )


if __name__ == "__main__":
    main()
