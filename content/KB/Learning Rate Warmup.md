---
tags: ['temp']
toc: true
title: Learning Rate Warmup
date modified: Monday, October 10th 2022, 2:02:23 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# Learning Rate Warmup
- Small learning rate at the start and then a larger learning rate when the training is stabilized
- Linearly from 0 to initial rate
- First m batches to warm up and if the initial learning rate is $\eta$ then at batch i, $1 \leq i \leq m$ , learning rate is $$\frac{i\eta}{m}$$



