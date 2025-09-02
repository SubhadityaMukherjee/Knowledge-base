---
toc: true
title: Cut and Mix
tags: ['augmentation']
date created: Sunday, October 9th 2022, 12:21:26 pm
date modified: Monday, October 10th 2022, 2:02:07 pm
---

# Cut and Mix
- @yunCutMixRegularizationStrategy2019
- instead of deleting a patch, the patch is replaced with some other image region
- y this approach, an image shares multiple class labels, whereas the major class label belongs to the original class label
- Hence, the model learns to differentiate between two classes within a single image.
- CutMix can be defined by the following operations $$\overset{\sim}x = M \odot x_{A} + (1-M) \odot x_{B}$$
- $$\overset{\sim}y = \lambda y_{A}+ (1- \lambda)y_{B}$$
- where $x$ is an RGB image, $y$ is the respective label, $M$ is a binary mask of the patch of the image that will be dropped and $\odot$ represents element wise multiplication. The new training sample $\overset{\sim}x , \overset{\sim}y$ is created by combining two other training samples $x_{A}, y_{A}$ and $x_{B} , y_{B}$. To control the combination ratio $\lambda$, a sample from the $\beta(1,1)$ distribution is chosen. This combination is quite similar to [Mixup](Mixup.md).
![](../images/Pasted%20image%2020230327152000.png)



