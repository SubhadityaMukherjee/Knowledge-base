---
toc: true
title: Test-time Augmentation
tags: ['augmentation']
date created: Monday, October 10th 2022, 1:58:13 pm
date modified: Monday, October 10th 2022, 2:02:06 pm
---

# Test-time Augmentation
- augmenting data at test-time as well
- This can be seen as analogous to ensemble learning techniques in the data space.
- By taking a test image and augmenting it in the same way as the training images, a more robust prediction can be derived.
- restrict the speed of the model
- promising practice for applications such as medical image diagnosis
- Radosavovic et al. denote test-time augmentation as data distillation to describe the use of ensembled predictions to get a better representation of the image.
- They also found better uncertainty estimation when using test-time augmentation, reducing highly confident but incorrect predictions.
- Matsunaga et al. also demonstrate the effectiveness of test-time augmentation on skin lesion classification, using [geometric transformations](geometric transformations.md) such as rotation, translation, scaling, and [Flipping](Flipping.md).
- A robust classifier is thus defined as having a low variance in predictions across augmentations
- In their experiments searching for augmentations with Reinforcement Learning, Minh et al. measure robustness by distorting test images with a 50% probability and contrasting the accuracy on un-augmented data with the augmented data.
- Some classification models lie on the fence in terms of their necessity for speed. This suggests promise in developing methods that incrementally upgrade the confidence of prediction. This could be done by first outputting a prediction with little or no testtime augmentation and then incrementally adding test-time augmentations to increase the confidence of the prediction.
- However, it is difficult to aggregate predictions on geometrically transformed images in object detection and semantic segmentation. Curriculum learning
- strategy for selecting training data that beats random selection
- best to initially train with the original data only and then finish training with the original and augmented data, although there is no clear consensus



