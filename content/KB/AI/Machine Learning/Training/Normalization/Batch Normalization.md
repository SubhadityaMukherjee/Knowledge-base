---
toc: true
title: Batch Normalization
tags:
  - normalization
date modified: Monday, October 10th 2022, 2:02:33 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# Batch Normalization

- bias=False for Linear/Conv2D for input and True for output #deeplearning
- Normalizes #architecture
- Input [[Distributions]] change per layer -> Make sure they stay similar
- Reduces co variate shift because now the network must adapt per layer
- During testing : use stats saved during training
- Simplifies learning dynamics
	- Can use larger learning rate
	- Higher order interactions are suppressed because the mean and std are independant of the activations which makes training easier
- Cant work with small batches. Not great with RNN
- ![[Pasted image 20220306114903.webp]]
- $$\mu_j \leftarrow \frac{1}{m}\Sigma_{i=1}^m x_{ij}$$
- $$\sigma^2_j \leftarrow \frac{1}{m}\Sigma^m_{i=1}(x_{ij}-\mu_j)^2$$
- $$\hat x_{ij} \leftarrow \frac{x_{ij}-\mu_j}{\sqrt{\sigma^2_j + \epsilon}}$$
- $$\hat x_{ij} \leftarrow \gamma \hat x_{ij} + \beta$$

## Why

- Stable forward prop
- Higher learning rates
- [[Regularization]]
