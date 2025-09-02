# Art Gallery Management Scripts

This directory contains scripts to help you manage your art gallery data for the Instagram-like layout.

## Files

- `update-art-data.js` - Main script for managing art data
- `parse-art-from-markdown.js` - Parse art from your existing My Art.md file

## Usage

### 1. Parse from existing markdown (Recommended first step)

If you already have art listed in your `My Art.md` file, run this to extract all the art data:

```bash
node scripts/parse-art-from-markdown.js
```

This will:
- Read your `My Art.md` file
- Extract all art entries (lines with `![[image.webp]]`)
- Generate `content/art-data.json` automatically

### 2. Scan for new images

To automatically add new images from your `art_images` directory:

```bash
node scripts/update-art-data.js scan
```

This will:
- Scan the `content/art_images/` directory
- Add any new image files to your art data
- Generate titles from filenames

### 3. Add art manually

To add a new art piece interactively:

```bash
node scripts/update-art-data.js add
```

This will prompt you for:
- Image filename
- Title
- Alt text

### 4. List current art

To see all your current art pieces:

```bash
node scripts/update-art-data.js list
```

## Art Data Format

Your art data is stored in `content/art-data.json` with this structure:

```json
[
  {
    "src": "art_images/boat_people.webp",
    "alt": "River people",
    "title": "River people"
  }
]
```

## Workflow

1. **Initial setup**: Run `parse-art-from-markdown.js` to extract from your existing markdown
2. **Adding new art**: 
   - Add image files to `content/art_images/`
   - Run `node scripts/update-art-data.js scan` to auto-add them
   - Or run `node scripts/update-art-data.js add` to add manually with custom titles
3. **Managing existing art**: Edit `content/art-data.json` directly or use the scripts
