---
toc: true
title: Sample Pairing
tags: ['augmentation']
date created: Sunday, October 9th 2022, 12:21:26 pm
date modified: Sunday, November 6th 2022, 5:19:35 pm
---

# Sample Pairing
- @inoueDataAugmentationPairing2018
- merges two images by averaging their pixel intensities
- The new image has the same training image label opposite to MixUp and other approaches where labels are updated according to the proportion of image mixing.
- one epoch on ImageNet and 100 epochs on other datasets are completed without SamplePairing before mixed image data is added to the training
- Once the SamplePairing images are added to the training set, they run in cycles between 8:2 epochs, 8 with SamplePairing images, 2 without.



