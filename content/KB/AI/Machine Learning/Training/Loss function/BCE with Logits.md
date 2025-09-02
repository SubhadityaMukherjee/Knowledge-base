---
toc: true
title: BCE Logits
tags: ['loss']
date modified: Monday, October 10th 2022, 2:02:34 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# BCE [[Logits]]
- [[Cross Entropy]] + [[Logits]]
$$\left( - \mathrm{sum}\left( y \cdot \mathrm{logsoftmax}\left( ŷ \right) \cdot weight \right) \right) \cdot \mathrm{//}\left( 1, \mathrm{size}\left( y, 2 \right) \right)$$

## …



