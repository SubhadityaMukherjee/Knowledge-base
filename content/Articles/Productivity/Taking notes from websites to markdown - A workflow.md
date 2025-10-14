
---
toc: true
title: Taking notes from websites to markdown - A workflow

tags: ["article"]
date modified: 
date created: 
---
Taking notes from websites to markdown - A workflow #inprogress #articles

## Why

## What we want

## Obsidian Quick intro

## Why markdown

## Chrome extension
[Extension](https://chrome.google.com/webstore/detail/markdownload-markdown-web/pcmpcfapbekmbjjkdalcgopdkipoggdi)
[Roam Highlighter](https://chrome.google.com/webstore/detail/roam-highlighter/mcoimieglmhdjdoplhpcmifgplkbfibp)

## Script
```py, webtomd_imports, webtomd_imports
import clipboard
import os
from pathlib import path
import re
```

```
def apply_transforms(txt, list_of_trans):
    for trans in list_of_trans:
        txt = trans(txt)
    return txt
```

```
def replacer(txt, dict_of_replace):
    for rep in dict_of_replace.keys():
        txt = txt.replace(rep, dict_of_replace[rep])
    return txt

def regexreplacer(txt, dict_of_replace):
    for rep in dict_of_replace.keys():
        txt = re.sub(rep, dict_of_replace[rep], txt)
    return txt
```

```
def indent_transform(txt):
    l = txt.split("\n")
    return "\n".join([x.strip() for x in l])
```

```
def paragraph_converter(txt):
    l = txt.split("\n")
    for item in range(len(l)):
        if len(l[item])>0 and l[item][0] not in ["#"," ",]:
            l[item] = "- "+l[item]
    return "\n".join(l)
```

## Practically Using it
```
dict_regex_replace = {
    r'\[.*?\]':"", #wiki links
}

dict_of_replace = {
    #"*": "",
    "- **": "# ",
    "**": "",
    "****": "",
    "[latex]": "$",
    "[/latex]": "$",
        "(<https://en.wikipedia.org/w/index.php?toc: true
title=":" ",
    "(https://en.wikipedia.org/w/index.php?toc: true
title=":" ",
    "s&action=edit&redlink=1":" ",
}
```

```
text = clipboard.paste()
text = replacer(text, dict_of_replace)
text = regexreplacer(text, dict_regex_replace)
text = apply_transforms(text, [
    indent_transform,
    paragraph_converter,
])
clipboard.copy(text)
```

## FAQ

### Why not a program?

## Fin
This article is in the hopes that it will help someone out. Maybe have the help that I did not. I do not know who it will reach. But to whoever it does, best of luck :)

Like these/Want more? Buy me a coffee! [Kofi](https://ko-fi.com/subhadityamukherjee)
Want articles on something specific? Just ask.
You can contact me on [LinkedIn](https://www.linkedin.com/in/subhaditya-mukherjee-a36883100), drop me an [[mailto:msubhaditya@gmail.com|Email]]



