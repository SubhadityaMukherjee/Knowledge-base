---
toc: true
title: AttributeMix
tags: ['augmentation']
date created: Sunday, October 9th 2022, 12:21:26 pm
date modified: Monday, October 10th 2022, 2:02:07 pm
---

- # AttributeMix
- [[@Attribute Mix: Semantic Data Augmentation for Fine Grained Recognition.md|@Attribute Mix: Semantic Data Augmentation for Fine Grained Recognition]]
- augments images based on se- mantically extracted image attributes
- Image is divided into a grid of patches where highly activated six responses are pasted onto the training image. These image pairs are selected randomly in every training iteration.
- attribute classifier by extracting k attributes (e.g., leg, head, and wings of a bird) from each image.
- The attribute mining procedure for every image is performed repetitively k times, whereas for each iteration, an attribute is masked out from the original image based on the most discriminative region in the attention map.
- attribute-level classifier is trained to generate new images for the actual classification model.

