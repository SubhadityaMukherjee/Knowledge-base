---
toc: true
title: Gradient Accumulation

tags: ['architecture']
date modified: Monday, October 10th 2022, 2:02:26 pm
date created: Thursday, July 28th 2022, 5:59:06 pm
---

# Gradient Accumulation
- [Pytorch](https://pytorch.org/docs/stable/notes/amp_examples.html)
- helps when the model is not able to be trained with a big enough batch size
- often caused by memory limitations of the [GPU](GPU)
- Accumulate the gradients (for each trainable model value) of several forward passes and after some steps use the accumulated gradients to update the weights
- Is then equal to using a large batch size
- example with $$SGD: \theta_{i}=\theta_{i}−1− \alpha\ast(\Sigma_{i=0}^{N}grad_{\theta_{i}})$$

