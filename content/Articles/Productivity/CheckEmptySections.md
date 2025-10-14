
---
toc: true
title: CheckEmptySections

tags: ["article"]
date modified: 
date created: 
---
# TODO

```python
import os
from pathlib import Path
import argparse as ap
import concurrent.futures
```

```python
ags = ap.ArgumentParser()
ags.add_argument("-f", help="File or folder name")
args = ags.parse_args()

mainpath = Path(args.f)
```

```python
# Check if the input is a directory or a file
if mainpath.is_dir() == True:
    # If it's a directory, create a list of Path objects for all the files in the directory
    all_files = [mainpath/Path(fl) for fl in os.listdir(mainpath)]
else:
    # If it's a file, create a list with a single Path object for the file
    all_files = [mainpath]
```

```python
def pipeline(txt_fn_list):
    """
    Applies a series of functions to a text.

    Parameters:
        txt_fn_list: A list containing the text to be processed as the first element, and the functions to be applied as the remaining elements.

    Returns:
        The final result of applying all the functions to the text.
    """
    # [txt, fn1, fn2....]
    txt = txt_fn_list[0]
    # Apply all fns one by one
    for fn in txt_fn_list[1]:
        txt = fn(txt)
    return txt
```

```python
def read_md(path):
    """
    Reads the contents of a Markdown file.

    Parameters:
        path: The path to the file.

    Returns:
        The contents of the file as a string.
    """
    print(path)
    try:
        with open(path, 'r') as fin:
            return fin.read()
    except:
        return None
```

```python
def check_blanks_hash(markdown):
    """
    Finds headers in a Markdown text that have no content under them.

    Parameters:
        markdown: The Markdown text to be processed.

    Returns:
        A list of headers that have no content under them.
    """
    if markdown != None:
        lines = markdown.split('\n')
        headers = []
        current_header = None
        current_content = []
        for line in lines:
            if line.startswith('#'):
                if current_header is not None:
                    headers.append({'header': current_header, 'content': " ".join(current_content)})
                current_header = line
                current_content = []
            else:
                current_content.append(line)
        if current_header is not None:
            headers.append({'header': current_header, 'content': " ".join(current_content)})
        
        # Return a list of headers that have no content under them
        return [header["header"] for header in headers if len(header["content"]) < 2]
    else:
        return None
```

```python
def main():
    pipe_fns = [read_md, check_blanks_hash]
    with concurrent.futures.ProcessPoolExecutor() as executor:
        # Start a process for each file and store the returned result in a list
        results = [executor.submit(pipeline, [file, pipe_fns]) for file in all_files]
        for future in concurrent.futures.as_completed(results):
            print(future.result())

if __name__ == '__main__':
    main()
```



