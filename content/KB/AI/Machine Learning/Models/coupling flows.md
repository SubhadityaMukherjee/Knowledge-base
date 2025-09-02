---
title: coupling flows
toc: true
tags:
  - distributions
date modified: Tuesday 19th November 2024, Tue
date created: Tuesday 19th November 2024, Tue
---

# Coupling Flows
```toc
```
- Consider a continuous random variable $z \in \mathbb{R}^D$
- Partition z into two subsets : eg two contiguous sub-vectors using a function g
- [[1ac5331e588254745dbd2898274013ed_MD5.webp|Open: Pasted image 20241119165521.png]]
![[1ac5331e588254745dbd2898274013ed_MD5.webp]]
- $$\begin{align*} x_{1:d}= z_{1:d} \\ x_{d+1:D}= g(z_{d+1:D}; m(z_{1:d})) \end{align*}$$
- elements in the first subset are not affected by those in the second
- to invert them is trivial $$\begin{align*} z_{1:d}= x_{1:d} \\ z_{d+1:D}= g^{-1}(x_{d+1:D}; m(x_{1:d})) \end{align*}$$
- [[Additive coupling layer]]
- [[Scaling matrix for coupling layers]]