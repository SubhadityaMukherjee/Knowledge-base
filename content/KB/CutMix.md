---
toc: true
title: CutMix
tags: ['augmentation']
date created: Sunday, October 9th 2022, 12:21:26 pm
date modified: Monday, October 10th 2022, 2:02:07 pm
---

# CutMix
- @yunCutMixRegularizationStrategy2019
- images are augmented by sampling patch coordinates, x, y, h, w from a uniform distribution
- selected patch is replaced at the
- corresponding location with a patch from the other randomly picked image from the current mini-batch during training.
- M is the image mask, xa and xb are images, λ is the proportion of label, and ya and yb are the labels of images.
- $$
x_{new}= M.x_{a}+(1-M).x_{b}
$$
- $$
y_{new}= \lambda.y_{a}+ (1-\lambda).y_{b}
$$



