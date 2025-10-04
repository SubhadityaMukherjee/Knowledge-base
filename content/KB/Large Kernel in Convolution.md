---
toc: true
title: Large Kernel in Convolution

tags: ['architecture']
date modified: Sunday, October 23rd 2022, 5:00:19 pm
date created: Sunday, October 23rd 2022, 5:00:18 pm
---

# Large Kernel in Convolution


- Global Convolutional Network (GCNs) (Peng et al., 2017) enlarges the kernel size to 15 by employing a combination of 1×M + M×1 and M×1 + 1×M convolutions.
- However, the proposed method leads to performance degradation on ImageNet
- or the utilization of varying convolutional kernel sizes to learn spatial patterns at different scales. With the popularity of VGG (Simonyan & Zisserman, 2014), it has been common over the past decade to use a stack of small kernels (1×1 or 3×3) to obtain a large receptive
- field
- However, the performance improvement plateaus when further expanding the kernel size
- Han et al. (2021b) find that dynamic depth-wise convolution (7x7) performs on par with the local attention mechanism if we substitute the latter with the former in Swin Transformer
- Liu et al. (2022b) imitate the design elements of Swin Transformer (Liu et al., 2021e) and design ConvNeXt employed with 7x7 kernels, surpassing the performance of the former
- Lately, Chen et al. (2022) reveal large kernels to be feasible and beneficial for 3D networks too.
- Prior works have explored the idea of paralleling (Peng et al., 2017; Guo et al., 2022a) or stacking (Szegedy et al., 2017) two complementary Mx1 and 1xM kernels
- However, they limit the shorter edge to 1 and do not scale the kernel size beyond 51x51



