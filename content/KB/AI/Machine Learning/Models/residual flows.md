---
title: residual flows
toc: true
tags:
  - architecture
date modified: Tuesday 19th November 2024, Tue
date created: Tuesday 19th November 2024, Tue
---

# Residual Flows
```toc
```
- inspiration from [[Res Net]]
- use [[Banach fixed point theorem]]

## Inverting Residual Network Layers
- form $h' = h + f[h, \phi]$ , if we ensure that $f[h, \phi]$ is a contraction mapping ([[Banach fixed point theorem]])
- [[lipschitz constant]] must be less than 1
- Assuming that the slope of the activation functions is not greater than one, this is equivalent to ensuring the largest eigenvalue of each weight matrix $\Omega$ must be less than 1
- ![[819bee748a5d469a3fe3de0d592947e5_MD5.webp]]