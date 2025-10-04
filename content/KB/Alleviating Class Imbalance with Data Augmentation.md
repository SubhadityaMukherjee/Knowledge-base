---
toc: true
title: Alleviating Class Imbalance with Data Augmentation
tags: ['augmentation']
date created: Monday, October 10th 2022, 1:58:13 pm
date modified: Monday, October 10th 2022, 2:02:06 pm
---

# Alleviating Class Imbalance with Data Augmentation
- Data Augmentation falls under a Data-level solution to class imbalance and there are many different strategies for implementation.
- A naive solution to oversampling with Data Augmentation would be a simple random oversampling with small [Geometric Transformations](Geometric%20Transformations.md) such as a 30° rotation
- One problem of oversampling with basic image transformations is that it could cause overfitting on the minority class which is being oversampled
- The biases present in the minority class are more prevalent post-sampling with these techniques.
- Neural Style Transfer is an interesting way to create new images. These new images can be created either through extrapolating style with a foreign style or by interpolating styles amongst instances within the dataset.
- Oversampling with GANs can be done using the entire minority class as 'real' examples, or by using subsets of the minority class as inputs to GANs
- The use of evolutionary sampling to find these subsets to input to GANs for class sampling is a promising area for future work.



