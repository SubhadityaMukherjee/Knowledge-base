---
toc: true
title: Kernel Filters
tags: ['augmentation']
date created: Monday, October 10th 2022, 1:58:12 pm
date modified: Tuesday, October 25th 2022, 12:11:48 pm
---

# Kernel Filters
- sharpen and blur images
- These filters work by sliding an n × n matrix across an image with either a Gaussian blur filter, which will result in a blurrier image, or a high contrast vertical or horizontal edge filter which will result in a sharper image along edges
- Intuitively, blurring images for Data Augmentation could lead to higher [Resistance](Resistance.md) to motion blur during testing
- Additionally, sharpening images for Data Augmentation could result in encapsulating more details about objects of interest.
- Kang et al. experiment with a unique kernel filter that randomly swaps the pixel values in an n×n sliding window. They call this augmentation technique PatchShuffle [Regularization](Regularization.md)



