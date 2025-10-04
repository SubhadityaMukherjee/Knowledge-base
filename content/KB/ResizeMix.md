---
toc: true
title: ResizeMix
tags: ['augmentation']
date created: Sunday, October 9th 2022, 12:21:26 pm
date modified: Monday, October 10th 2022, 2:02:07 pm
---

# ResizeMix

- @qinResizeMixMixingData2020
- performs random image [Cropping](Cropping.md) and pasting
- ResizeMix solves the random region [Cropping](Cropping.md) problem that misallocates the output image label in certain cases where the pasted region does not contain any object informa- tion
- scaling down (scale rate is sampled from a uniform dis- tribution) the selected image completely and past- ing it randomly on the target image
- modified labels of the output image are always accurate and proportionate to the mixing.



