---
toc: true
title: CycleGAN

tags: ['architecture']
date modified: Wednesday, December 14th 2022, 11:20:53 am
date created: Sunday, December 11th 2022, 12:58:09 pm
---

# CycleGAN

- Unpaired image2image
- 2 Mapping functions G, F : generator and $D_{X}, D_{Y}$ as generators
- [Adversarial Loss](Adversarial Loss.md)
- $\mathcal{L}_{cyc}$ [Cycle Consistency Loss](Cycle Consistency Loss.md)
- Full objective
	- Adversarial Loss + [Cycle Consistency Loss](Cycle Consistency Loss.md)
	- $\lambda$ is a hyperparam. Generally set to 10
	- $$\mathcal{L}_{GAN}(G, F, D_{X}, D_{Y}) = \mathcal{L}_{GAN}(G, D_{Y}, X, Y) + \mathcal{L}_{GAN}(F, D_{X}, X, Y) + \lambda \mathcal{L}_{cyc}(G,F)$$
- To Solve
- $$G^{*},F^{*} =\underset{G,F}{argmin} \underset{D_{X}, D_{Y}}{max} \mathcal{L}_{GAN}(G, F, D_{X}, D_{Y})$$
- two stride-2 convolutions, several residual blocks, and two fractionally [Strided](Strided.md) convolutions with stride $\frac{1}{2}$
- [Instance Normalization](Instance Normalization.md)

## Architecture

## Generator
- ![](../images/Pasted%20image%2020221211132006.png)

### Encoder
- The encoder extracts features from the input image by using Convolutions and compressed the representation of image but increase the number of channels
- The encoder consists of 3 convolution that reduces the representation by 1/4 th of actual image size

### Transforming Block
- The transformer contains 6 or 9 residual blocks based on the size of input.
- The output of transformer is then passed into the decoder which uses 2 -deconvolution block of fraction strides to increase the size of representation to original size.

## Discriminator
- [PatchGAN](PatchGAN.md)

## Applications
- Style Transfer
	- Unlike other works on neural style transfer, CycleGAN learns to mimic the style of an entire collection of artworks, rather than transferring the style of a single selected piece of art
- Object Transformation
	- CycleGAN can transform object from one ImageNet class to another such as: Zebra to Horses and vice-versa, Apples to Oranges and vice versa etc
- Season Transfer
	- CycleGAN can also transfer images from Winter Season to Summer season and vice-versa. For this the model is trained on 854 winter photos and 1273 summer photos of Yosemite from Flickr.
- Photo Generation from Painting
	- can also be used to transform photo from paintings and vice-versa
	- [Identity Loss](Identity Loss.md)

## Limits
- applied to perform geometrical transformation, CycleGAN does not perform very well. This is because of the generator architecture which is trained to perform appearance changes in the image.

## Reduce Model Oscillation
- To prevent the model from changing drastically from iteration to iteration, the discriminators were fed a history of generated images, rather than just the ones produced by the latest versions of the generator.
- To do this we keep storing the 50 most recently generated images. Based on this technique we reduce the model Oscillation as well as model overfitting.

## Technical Implementation

The CycleGAN paper provides a number of technical details regarding how to implement the technique in practice.

The generator network implementation is based on the approach described for style transfer by [Justin Johnson](https://cs.stanford.edu/people/jcjohns/) in the 2016 paper toc: true
titled “[Perceptual Losses for Real-Time Style Transfer and Super-Resolution](https://arxiv.org/abs/1603.08155).”

The generator model starts with best practices for generators using the deep convolutional GAN, which is implemented using multiple residual blocks (e.g. from the [ResNet](https://machinelearningmastery.com/how-to-implement-major-architecture-innovations-for-convolutional-neural-networks/)).

The discriminator models use [PatchGAN](PatchGAN.md), as described by [Phillip Isola](http://web.mit.edu/phillipi/), et al. in their 2016 paper toc: true
titled “[Image-to-Image Translation with Conditional Adversarial Networks](https://arxiv.org/abs/1611.07004).”

> This discriminator tries to classify if each NxN patch in an image is real or fake. We run this discriminator convolutionally across the image, averaging all responses to provide the ultimate output of D.

— [Image-to-Image Translation with Conditional Adversarial Networks](https://arxiv.org/abs/1611.07004), 2016.

PatchGANs are used in the discriminator models to classify 70×70 overlapping patches of input images as belonging to the domain or having been generated. The discriminator output is then taken as the average of the prediction for each patch.

The adversarial loss is implemented using a least-squared loss function, as described in [Xudong Mao](https://xudongmao.github.io/), et al’s 2016 paper toc: true
titled “[Least Squares Generative Adversarial Networks](https://arxiv.org/abs/1611.04076).”

> […] we propose the Least Squares Generative Adversarial Networks (LSGANs) which adopt the least squares loss function for the discriminator. The idea is simple yet powerful: the least squares loss function is able to move the fake samples toward the decision boundary, because the least squares loss function penalizes samples that lie in a long way on the correct side of the decision boundary.

— [Least squares generative adversarial networks](https://arxiv.org/abs/1611.04076), 2016.

Additionally, a buffer of 50 generated images is used to update the discriminator models instead of freshly generated images, as described in [Ashish Shrivastava’s](https://www.linkedin.com/in/ashish-shrivastava-3499127/) 2016 paper toc: true
titled “[Learning from Simulated and Unsupervised Images through Adversarial Training](https://arxiv.org/abs/1612.07828).”

> […] we introduce a method to improve the stability of adversarial training by updating the discriminator using a history of refined images, rather than only the ones in the current minibatch.

— [Learning from Simulated and Unsupervised Images through Adversarial Training](https://arxiv.org/abs/1612.07828), 2016.

The models are trained with the [Adam version of stochastic gradient descent](https://machinelearningmastery.com/adam-optimization-algorithm-for-deep-learning/) and a small learning rate for 100 epochs, then a further 100 epochs with a learning rate decay. The models are updated after each image, e.g. a batch size of 1.



