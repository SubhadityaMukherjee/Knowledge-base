---
toc: true
title: Cutout
tags: ['augmentation']
date created: Sunday, October 9th 2022, 12:21:26 pm
date modified: Monday, October 10th 2022, 2:02:07 pm
---

# Cutout
- @devriesImprovedRegularizationConvolutional2017
- removes constant size square patches randomly by replacing them with any constant value.
- The selection of region is performed by selecting a pixel value randomly and placing a square around it
- Cutout can be expressed as an element-wise multiplication operation $x_{cutout} = x \odot M$, where $x$ is the original image, $M$ is a binary mask of the same size as $x$ with randomly chosen coordinates of a square patch of pixels to be cut out, and $\odot$ denotes element-wise multiplication.



