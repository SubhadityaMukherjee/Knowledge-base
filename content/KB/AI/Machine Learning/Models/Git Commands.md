---
toc: true
title: Git Commands
tags:
  - architecture
date modified: Thursday 19th October 2023, Thu
date created: Thursday 19th October 2023, Thu
---

# Git Commands


-  Sources
	- [The Essential GitHub CLI Commands](https://blog.mergify.com/the-essential-github-cli-commands/)

## Managing Gists
```
gh gist create my\_mergify\_gist.py
```
```
gh gist create --public my\_mergify\_gist.py
```

### List All Your Gists
```
gh gist list
```
- You can also apply filters on this list using the `--limit int` argument (default to 10) along with the `--public` and `--secret` flags.

### View
```
gh gist view 4b5ba0b5daabf386ee01bc37ab667e58
```

### Delete
```
gh gist delete 4b5ba0b5daabf386ee01bc37ab667e58
```

## Managing Issues

### Creating an Issue
```
gh issue create --toc: true
title "Is it a bug?" --body "the behavior’s description"
```

### Listing All the repository’s Issues
```
gh issue list
```
- You can even open your browser with `--web`

### Status
```
gh issue status
```

### Closing an Issue
```
gh issue close <num>
```

### Reopening an Issue
```
gh issue reopen <num>
```

## Managing Repositories

### Create a Public Repository
```
gh repo create
```

### Forking a Repository
```
gh repo fork Mergifyio/react-crisp
```

### Listing the Repository of an account
```
gh repo list CamClrt
```
- You can filter this list down using the `--archived`, `--no-archived`, or `--source` flags.

## Managing PRs

### Creating a Pull Request with a Specific Title and Body
```
gh pr create --toc: true
title "feat: my\_super\_feature" --body "all the details" 
```

### Listing All the Pull Requests in the Repository
```
gh pr list
```
- this command allows you to apply a large number of filters like `--assignee`, `--base`, `--label`, and more

### Status of Your Pull Requests
```
gh pr status
```

### Getting a Pull Request to Inspect it
```
gh pr checkout 2530
```

### Displaying Continuous Integration (CI) Status for a Specific Pull Request
```
gh pr checks 1234
```

### Diff
```
gh pr checkout <num>
gh pr diff
```

### Merge
```
gh pr merge <num>
```

```
gh pr merge -m -d &lt;number&gt; &amp;&amp; git pull
```

### Display the Title, Body, and other Information about a Pull Request.
```
gh pr view
```

### Make a Pull Request as Ready for Review
```
gh pr ready
```

### Add a Review to a Pull Request
```
gh pr review
```

### Close/reopen
```
gh pr <close, reopen>
```
