---
toc: true
title: Intra-Class Part Swapping
tags: ['augmentation']
date created: Sunday, October 9th 2022, 12:21:26 pm
date modified: Monday, October 10th 2022, 2:02:07 pm
---

# Intra-Class Part Swapping
- @zhangIntraClassPartSwapping2021
- replaces most attentive regions of one image by the other
- Attentive regions are extracted using a classification activation map (CAM), thresholded for the most prominent region
- The attentive region in the source image is scaled and translated according to the attentive region of the target image for region replacement
- The label information of the output is similar to the target image as this approach relies on augmenting similar class images.



