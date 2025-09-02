---
tags: ['temp']
toc: true
title: Distillation Loss
date modified: Monday, October 10th 2022, 2:02:29 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# Distillation Loss
- $$\mathscr{l}(p, softmax(z))+T^{2}\mathscr{l}(softmax(\frac{r}{T}), softmax(\frac{z}{T}))$$
- Negative [Cross Entropy](Cross%20Entropy.md) + other
- p is the true [Probability](Probability.md) [Distributions](Distributions.md)
- z,r are outputs of the student and teacher model
- T is the temperature to make [Softmax](Softmax.md) smoother



