---
toc: true
title: MobileOne

tags: ['architecture']
date modified: Monday, October 10th 2022, 2:02:22 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# MobileOne
- [An Improved One Millisecond Mobile Backbone](https://arxiv.org/abs/2206.04040)
- extensive analysis of different metrics by deploying several mobile friendly networks on a mobile device
- identify and analyze architectural and optimization bottlenecks
- many times faster on mobile
- Inspired by[RepVGG](RepVGG.md)
- Either [Relu](Relu.md) or SE-[Relu](Relu.md) is used as activation. The trivial over-parameterization factor $k$ is a hyperparameter which is tuned for every variant.
- better top-1 accuracy on [ImageNet](ImageNet.md) than [EfficientNet](EfficientNet.md) at similar latency
- ![](../images/Pasted%20image%2020220620164552.jpg)



