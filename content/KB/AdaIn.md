---
toc: true
title: AdaIn

tags: ['regularization']
date modified: Monday, October 10th 2022, 2:02:35 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# AdaIn
- [paper](https://arxiv.org/abs/1703.06868v2)
- $$AdaIN(x,y) = \sigma(y) \big( \frac{x-\mu(x)}{\sigma (x)} \big)$$
- Adaptive [Instance Normalization](Instance%20Normalization.md) is a normalization method that aligns the mean and variance of the content [Features](Features.md) with those of the style [Features](Features.md).
- no learnable affine [Features](Features.md)
- Adaptively computes affine params from style input



