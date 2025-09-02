---
toc: true
title: MSLE
tags: ['loss']
date modified: Monday, October 10th 2022, 2:02:23 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# MSLE
- [MSE](MSE.md) log error
- Use MSLE when doing regression, believing that your target, conditioned on the input, is normally distributed, and you don’t want large errors to be significantly more penalized than small ones, in those cases where the range of the target value is large.

$$\frac{1}{\mathrm{length}\left( y \right)} \cdot \mathrm{sum}\left( \left( \log\left( y + 1 \right) - \log\left( ŷ + 1 \right) \right)^{2} \right)$$



