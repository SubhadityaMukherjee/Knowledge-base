---
toc: true
title: SmoothMix
tags: ['augmentation']
date created: Sunday, October 9th 2022, 12:21:26 pm
date modified: Monday, October 10th 2022, 2:02:07 pm
---

# SmoothMix
- @leeSmoothMixSimpleEffective2020
- mask-based approach
- matching closely with the [Cutout] and [CutMix](Cutout] and [CutMix.md) techniques
- the mask has soft edges with gradually decreasing intensity
- the mixing strategy is the same
- The augmented image has mixed pixel values depending on the strength of the mask
- $$\lambda= \frac{\Sigma_{i=1}^{W}\Sigma_{j=1}^{H}G_{ij}}{WH}$$
- Gij is the pixel value of mask G, H is height, and W is width
- xnew = G.xa + (1 − G).xb
- ynew = λ.ya + (1 − λ).yb



