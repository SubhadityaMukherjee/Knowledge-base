---
title: PixelShuffle
toc: true
tags:
  - architecture
date modified: Monday 30th September 2024, Mon
date created: Monday 30th September 2024, Mon
---

# PixelShuffle
```toc
```
- Conv filters with a stride of $1/s$ to scale up 1D signals by a factor of s.
- Only the weights that lie exactly on positions are used to create the outputs, and the ones that fall between positions are discarded. 
- This can be implemented by multiplying the number of channels in the kernel by a factor of s, where the sth output position is computed from just the sth subset of channels. 
- This can be trivially extended to 2D convolution, which requires s2 channels