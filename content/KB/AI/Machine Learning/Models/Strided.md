---
toc: true
title: Strided
tags: ['architecture']
date modified: Saturday, December 17th 2022, 1:59:23 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# Strided
- ![[Pasted image 20241002112411.webp]]
- Normally S = 1
- S>1 -> [Downsampling](Downsampling.md)
- Dilated
- Spaces in the filter kernel
- D = 1 : normal [Conv](Conv.md) aka D-1 spaces
- Effective Filter size : $$\hat F = F + (F-1)(D-1)$$
- ![](../images/036AB58B-7EF0-4F12-AE56-7BFA00DA1967.png)



