---
title: Atrous Convolution
toc: true
tags:
  - architecture
date modified: Monday 30th September 2024, Mon
date created: Monday 30th September 2024, Mon
---

# Atrous Convolution
```toc
```
- The kernel size can be increased to integrate over a larger area
- However, it typically remains an odd number so that it can be centered around the current position. Increasing the kernel size has the disadvantage of requiring more weights. 
- This leads to the idea of dilated or atrous convolutions, in which the kernel values are interspersed with zeros.
- The number of zeros we intersperse between the weights determines the dilation rate