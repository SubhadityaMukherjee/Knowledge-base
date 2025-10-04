---
toc: true
title: Manifold MixUp
tags: ['augmentation']
date created: Sunday, October 9th 2022, 12:21:26 pm
date modified: Monday, October 10th 2022, 2:02:07 pm
---

# Manifold MixUp
- mixes feature values generated from intermediate neural network layers.
- feedforward up to k layer of the network where the output feature maps are mixed
- The mixed feature maps are given input to the next layer and forward propagated up to the last layer.
- After the forward propagation, backward propagation is performed in the standard way with updated labels



