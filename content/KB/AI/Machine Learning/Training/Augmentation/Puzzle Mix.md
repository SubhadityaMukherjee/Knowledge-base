---
toc: true
title: Puzzle Mix
tags: ['augmentation']
date created: Sunday, October 9th 2022, 12:21:26 pm
date modified: Monday, October 10th 2022, 2:02:07 pm
---

# Puzzle Mix
- @kimPuzzleMixExploiting2020
- learns to augment two images optimally based on saliency.
- Images are divided into regions for the mixup
- The algorithm learns to transport the salient region of one image such that the output image has the maximized saliency from both images.
- $$h(x_{0}, x_{1}) = (1-z) \odot \Pi_{0}^{T}x_{0} + z \odot \Pi_{1}^{T}x_{1}$$
- where $z_{i}$ is a binary mask, $\lambda = \frac{1}{n}\Sigma_{i}z_{i}$ is the mixing ratio and $\Pi_{0}, \Pi_{1}$ are represent $n \times n$ grids that denote the amount of mass that is transported during transport of the image patch to another location. 



