---
tags: ['temp']
toc: true
title: Large Batch Training
date modified: Monday, October 10th 2022, 2:02:24 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# Large Batch Training
- Generally slows down training
- If convex, convergence rate decreases with increase in batch size
- [Learning Rate Scheduling](Learning%20Rate%20Scheduling.md)
- Modified [Batch Normalization](Batch%20Normalization.md) with $\gamma=0$ for all BNs at the end of a residual block that micmics networks with less [Layers](Layers.md) and is easier to train at the start
- [No bias decay](No%20bias%20decay.md)



