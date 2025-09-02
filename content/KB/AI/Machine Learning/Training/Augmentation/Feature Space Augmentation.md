---
toc: true
title: Feature Space Augmentation
tags: ['augmentation']
date created: Monday, October 10th 2022, 1:58:12 pm
date modified: Monday, October 10th 2022, 2:00:59 pm
---

# Feature Space Augmentation
- The sequential processing of neural networks can be manipulated such that the intermediate representations can be separated from the network as a whole. The lower-dimensional representations of image data in fully-connected layers can be extracted and isolated.
- DeVries and Taylor tested their feature space augmentation technique by extrapolating between the 3 nearest neighbors per sample to generate new data and compared their results against extrapolating in the input space and using affine transformations in the input space
- Vector representations are then found by training a CNN and then passing the training set through the truncated CNN. These vector representations can be used to train any machine learning model from Naive Bayes, Support Vector Machine, or back to a fully-connected multilayer network.
- A disadvantage of feature space augmentation is that it is very difficult to interpret the vector data.



