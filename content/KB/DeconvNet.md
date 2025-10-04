---
toc: true
title: DeconvNet

tags: ['explainability']
date modified: Tuesday, December 6th 2022, 12:04:42 pm
date created: Wednesday, October 12th 2022, 4:17:49 pm
---

# DeconvNet
```toc
  ```
- @zeilerVisualizingUnderstandingConvolutional2013
- Zeiler, Fergus

## Summary
- Deconvnets are designed to work similar to convolutional networks but reverse (reversing pooling component, reversing filter component etc.), and they can be trained using an unsupervised approach.
- To reconstruct the activation on a specific layer, we are attaching deconv layers to corresponding CNN layers
- To examine a reconstruction for a given class c, we have to set all activations except the one responsible for predicting class c to zero.
- Then we can propagate through deconvnet layers and pass all the feature maps as inputs to corresponding layers
- Propagation through the whole deconvnet gives us a representation of the features from the first layer of the original CNN
- This approach causes the saliency map to feature some biases from the first convolutional layer and the representation looks like a localized edge detector
- works better when there is a clear distinction in the feature importance rather than similar values for the whole image
- Basically invert operations between input and the chosen layer.
	- Conv -> Deconv
	- Pool -> Unpooling
	- ReLU -> ReLU with negative valyes clamped going backward from the activation space to image space
	- Pooling is non invertible, but uses a switch module : recover positions of maxima in the forward pass
- DeconvNet is a calculation of a backward convolutional network that reuses the weights at each layer from the output layer back to the input image
- The employed mechanisms are deconvolution and unpooling, which are especially designed for CNNs with convolutions, max-pooling, and Rectified Linear Units (ReLUs). The method makes it possible to create feature maps of an input image that activates certain hidden units most, linked to a particular prediction
- With their propagation technique, they identified the most responsible patterns for this output. The patterns are visualized in the input space
- DeconvNet is limited to max-pooling layers, but the unpooling uses an approximate inverse

## Filtering 
- Filtering in the original CNN computes feature maps using learned filters. Reversing that operation requires the use of a transposed version of the same filters. Those transposed filters are then applied to the Rectified Unpooled Maps.

## Rectification 
- same ReLU non-linearity
- simply just rectifying the values and propagate only non-negative ones to the filtering layer

## Unpooling 
- The original max-pooling operation is non-invertible, but this approach uses additional variables called switch variables, which are responsible for remembering the locations of the maxima for each pooling region.

## Images

- ![](../images/1!yfVt0dZ8X6h6WoDFlyAqsw.png)
- ![](../images/Pasted%20image%2020221012161759.png)



