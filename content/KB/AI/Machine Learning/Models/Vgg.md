---
toc: true
title: Vgg
tags: ['architecture']
date modified: Monday, October 10th 2022, 2:02:14 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# Vgg
- @simonyanVeryDeepConvolutional2014
- [Very Deep Convolutional Networks for Large-Scale Image Recognition](https://arxiv.org/abs/1409.1556)
- Deeper [Alex Net](Alex%20Net.md)
- Object detection and Image captioning
- 5x5 -> two 3x3
- No of filters increase according to depth
- No of filters : increase by power of two
- Filter size : Odd numbers
- SGD + LR Schedule
- three non-linear activations (instead of one), which makes the function more discriminative
- ![[Pasted image 20241002114234.webp]]