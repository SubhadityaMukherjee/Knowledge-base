import os
import re
from pathlib import Path

# Directory to search for markdown files
vault_dir = Path("/Users/smukherjee/Documents/CODE/Github/AI-knowledge-base/posts")
with open("tag_lists.md", "r") as f:
    words_to_search = f.readlines()

# Tags to search for
# for each markdown file recursively in the vault directory, search for the tags in the first 10 line and create a dictionary of tags and the file names
tag_dict = {}
for root, dirs, files in os.walk(vault_dir):
    for file in files:
        if file.endswith(".md"):
            with open(os.path.join(root, file), "r") as f:
                lines = f.readlines()[:10]
                for line in lines:
                    for word in words_to_search:
                        if re.search(word, line, re.IGNORECASE):
                            if word in tag_dict:
                                tag_dict[word].append(file)
                            else:
                                tag_dict[word] = [file]

# make the tag_dict values unique
for key in tag_dict:
    tag_dict[key] = list(set(tag_dict[key]))
    # sort
    tag_dict[key].sort()

# Create a directory to store the tag pages
tag_dir = Path(
    "/Users/smukherjee/Documents/CODE/Github/AI-knowledge-base/posts/Tag Pages"
)

# Create a markdown file for each tag and list the files that contain the tag.
for tag, files in tag_dict.items():
    with open(tag_dir / f"{tag}.md", "w") as f:
        f.write(f"# {tag.capitalize()}\n\n")
        for file in files:
            file_name = Path(file).stem.strip()
            if file_name != tag:
                # print(file_name)
                # exit(0)
                # f.write(f'- [{file.name}](file.name})\n')
                f.write(f"- [[{file_name}]] \n")
