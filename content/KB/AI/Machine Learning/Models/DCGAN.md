---
toc: true
title: DCGAN

tags: ['architecture']
date modified: Saturday, December 17th 2022, 12:46:45 pm
date created: Tuesday, December 13th 2022, 5:02:02 pm
---

# DCGAN


## Architecture
- ![](../images/F5FD8256-22A4-45E2-A635-E1B8BD48C0AB.png)

### Weight Init
- If conv Random Normal with mean = 0 and std.dev = 0.02
- If BatchNorm with mean = 1.0 and std.dev = 0.02, Bias = 0

### Generator
- Map latent space vector z to data space
- Creating RGB with same size as training image
- [Transposed Conv] , [Batch Normalization] and [Relu](Transposed Conv] , [Batch Normalization] and [Relu.md)
- Output is 3x64x64
- Output passed through [Tanh](Tanh.md) to return it to [-1,1]
- [Batch Normalization] AFTER [Transposed Conv](Batch Normalization] AFTER [Transposed Conv.md) is super important as it helps with flow of gradients
- Notice, how the inputs we set in the input section (_nz_, _ngf_, and _nc_) influence the generator architecture in code. _nz_ is the length of the z input vector, _ngf_ relates to the size of the feature maps that are propagated through the generator, and _nc_ is the number of channels in the output image (set to 3 for RGB images)
- ![](../images/0A6407EB-22F6-4D06-AB2E-E99EF94E25C0.png)

### Discriminator
- [Strided] [Conv], [Batch Normalization], and [Leaky Relu](Strided] [Conv], [Batch Normalization], and [Leaky Relu.md)
- 3x64x64 input
- Binary classification network - outputs prob of real/fake
- Final is a [Sigmoid](Sigmoid.md) layer
- For [downsampling], good Practise to use [Strided] rather than [Pooling](downsampling], good Practise to use [Strided] rather than [Pooling.md) as it lets the network learn it's own pooling function
- Almost a direct inverse of the Generator

## Special Features
-   Explicitly uses convolutional layers in the discriminator and transposed-convolutional layers in the generator
-   Further the discriminator uses batch norm layers and [Leaky Relu] activations while the generator uses [Relu](Leaky Relu] activations while the generator uses [Relu.md) activations
-   The input is a latent vector drawn from a standard [normal distribution](normal distribution.md) and the output is a $3 \times 32 \times 32$ RGB image
-   In this implementation, I also added in [Label Smoothing](Label Smoothing.md)

## Loss functions

### Discriminator [loss](../Tag%20Pages/loss.md)
The Discriminator penalizes wrongly classifying a real image as a fake or a fake image as real. This can be thought of as maximizing the following function.
$$\nabla_{\theta_{d}} \frac{1}{m} \Sigma_{i=1}^{m}[log D(x^{(i)}) + log(1-D(G(z^{(i)})))]$$
  

### Generator [loss](../Tag%20Pages/loss.md)
- The Generator loss takes the output of the Discriminator into account and rewards it if the Generator is fooled into thinking the fake image is real. If this condition is not satisfied, the Generator is penalized.

- This can be thought of as minimizing the following function.
$$\nabla_{\theta_{g}} \frac{1}{m} \Sigma_{i=1}^{m}log(1-D(G(z^{(i)})))$$



