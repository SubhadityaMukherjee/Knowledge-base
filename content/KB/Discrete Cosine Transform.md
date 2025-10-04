---
toc: true
title: Discrete Cosine Transform

tags: ['temp']
date modified: Monday, October 10th 2022, 2:02:29 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# Discrete Cosine Transform
- [machine-learning-articles/cnns-and-feature-extraction-the-curse-of-data-sparsity.md at main · christianversloot/machine-learning-articles](https://github.com/christianversloot/machine-learning-articles/blob/main/cnns-and-feature-extraction-the-curse-of-data-sparsity.md) #[Roam-Highlights](Roam-Highlights)
- expresses a finite sequence of data points in terms of a sum of cosine functions oscillating at different frequencies
	- you make the CNN blind to the unique aspects represented by the numbers… despite the fact that they are already in there
	- In my opinion, this can be explained by looking at the internals of a convolutional layer. It works as follows. You specify a number of filters which, during training, learn to recognize unique aspects of the image-like data. They can then be used to classify new samples - quite accurately, as we have seen with raw [MNIST](MNIST.md) data. This means that the convolutional layer already makes your data representation sparser. What's more, this effect gets even stronger when [Layers](Layers.md) like [Pooling](Pooling.md) are applied
	- But when you downsample the data first by e.g. applying the DCT, you thus effectively apply sparsening twice. My only conclusion can thus be that by consequence, the convolutional filters can no longer learn the unique aspects within the image-like data, as they are hidden in the data set made compact. Only then, I literally found out why people always suggest to input your [Image Data](Image%20Data.md) into CNNs as untransformed as possible.
	- Besides the architectural differences between them, one must also conclude that CNNs make data essentially sparser while SVMs do not.



