---
toc: true
title: Smart Augmentation
tags: ['augmentation']
date created: Monday, October 10th 2022, 1:58:12 pm
date modified: Monday, October 10th 2022, 2:02:06 pm
---

# Smart Augmentation
- utilizes a similar concept as the [Neural Augmentation](Neural Augmentation.md) technique
- However, the combination of images is derived exclusively from the learned parameters of a prepended CNN, rather than using the Neural Style Transfer algorithm.
- another approach to meta-learning augmentations
- This is done by having two networks, Network-A and Network-B. Network-A is an augmentation network that takes in two or more input images and maps them into a new image or images to train Network-B. The change in the error rate in Network-B is then
- backpropagated to update Network-A.
- Additionally another loss function is incorporated into Network-A to ensure that its outputs are similar to others within the class. Network-A uses a series of convolutional layers to produce the augmented image
- The conceptual framework of Network-A can be expanded to use several Networks trained in parallel. Multiple Network-As could be very useful for learning class-specific augmentations via meta-learning



