---
toc: true
title: Random Erasing
tags: ['augmentation']
date created: Sunday, October 9th 2022, 12:21:26 pm
date modified: Monday, October 10th 2022, 2:00:29 pm
---

# Random Erasing
- @zhongRandomErasingData2020
- deletes contiguous rectangular image regions similar to [Cutout](Cutout.md) with minor differences in region selection procedure.
- Opposite to [Cutout](Cutout.md), where deletion is applied on all the images, here it is performed with a probability of either applying it or not
- In every iteration, region size is defined randomly with upper and lower limits on region area and aspect ratio.
- Additional to this, random erasing provides region-aware deletion for object detection and person identification tasks
- Regions inside the object bounding boxes are randomly erased to generate occlusions



