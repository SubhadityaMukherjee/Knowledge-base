---
toc: true
title: Primary Capsule

tags: ['architecture']
date modified: Sunday 12th February 2023, Sun
date created: Sunday 12th February 2023, Sun
---

# Primary Capsule


- lowest layer of a capsule network 
- processing the **raw input image**
- Each capsule in the primary layer is sensitive to a specific feature of the input image, such as an edge or a particular shape.

### Convolution 
- The primary capsules in a capsule network are created by applying a series of convolutional filters to the input image. Each filter is responsible for detecting a specific feature in the input image, such as an edge or a particular shape.

## Reshape
- The outputs of the convolutional filters are then reshaped into a grid of “capsules,” each of which corresponds to a specific location in the input image.

## Squash
- The outputs of the capsules are then “squashed” to ensure that they have a non-negative scalar value, which allows the network to learn more easily to differentiate between objects and background.



