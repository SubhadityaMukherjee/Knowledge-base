---
toc: true
title: Strided Attention

tags: ['architecture']
date modified: Monday, October 10th 2022, 2:02:16 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# [Strided](Strided.md) [Attention](Attention.md)
- [paper](https://arxiv.org/abs/1904.10509v1)
- Sparse factorizations of the [Attention](Attention.md) matrix
- Reduce to $O(n\sqrt{n})$
- Recompute [Attention](Attention.md) matrices to save memory
- Fast [Attention](Attention.md) kernels
- Works nicely for images, music etc with a periodic structure
- Otherwise with the [Strided](Strided.md) pattern , the spatial coordinates do not correlate with the positions the elements might be more relevant in the future
- ![](../images/Pasted%20image%2020220621175944.png)



