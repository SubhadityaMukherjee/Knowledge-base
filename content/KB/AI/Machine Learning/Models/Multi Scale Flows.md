---
title: Multi Scale Flows
toc: true
tags:
  - architecture
date modified: Tuesday 19th November 2024, Tue
date created: Tuesday 19th November 2024, Tue
---

# Multi Scale Flows
```toc
```

![[d97fdb6066a004741e909f851cbd6b4b_MD5.webp]]

- The first partition z1 is processed by a series of reversible layers with the same dimension as z1 until, at some point, z2 is appended and combined with the first partition.
- This continues until the network is the same size as the data x. 
- In the normalizing direction, the network starts at the full dimension of x, but when it reaches the point where zn was added, this is assessed against the base distribution