---
toc: true
title: Cropping
tags: ['augmentation']
date created: Monday, October 10th 2022, 1:58:12 pm
date modified: Monday, October 10th 2022, 2:00:43 pm
---

# Cropping
- Cropping images can be used as a practical processing step for image data with mixed height and width dimensions by cropping a central patch of each image
- Additionally, random cropping can also be used to provide an effect very similar to translations.
- whereas translations preserve the spatial dimensions of the image
- Depending on the reduction threshold chosen for cropping, this might not be a label-preserving transformation. Rotation
- Rotation augmentations are done by rotating the image right or left on an axis between 1° and 359°
- The safety of rotation augmentations is heavily determined by the rotation degree parameter.
- as the rotation degree increases, the label of the data is no longer preserved post-transformation. Translation
- Shifting images left, right, up, or down can be a very useful transformation to avoid positional bias in the data
- For example, if all the images in a dataset are centered, which is common in face recognition datasets, this would require the model to be tested on perfectly centered images as well.
- remaining space can be filled with either a constant value such as 0 s or 255 s, or it can be filled with random or Gaussian noise



