---
toc: true
title: Salience Map

tags: ['explainability']
date modified: Friday, November 18th 2022, 1:30:54 pm
date created: Wednesday, October 12th 2022, 4:38:39 pm
---

# Salience Map


## Explained
- Specifies parts of the image that contribute the most to the activity of a specific layer or the entire decision
- $Y_{c}=\text{score of class c}$ : value of output before softmax
- $$saliency = max_{r,g,b}(|\frac{\partial Y_{c}}{\partial I}|)$$
- grad of $Y_{c}$ wrt input - matrix with shape similiar to input
- if value close to 0 : small changes in input have no effect on output
- if high magnitude : small changes can have a major impact
- positive : roughly the location of the target object
- negative : competing class objects : background or instance
- Abs value for heatmap
- grads : backprop on $Y_{c}$ instead of loss

## Three Approaches

### Dencov
- Use [DeconvNet](DeconvNet.md)
- Use backprop to compute the gradients of logits wrt input : [Deep Inside Convolutional Networks](Deep Inside Convolutional Networks.md)
- [Guided BackProp](Guided BackProp.md)

## Features
- One of the oldest interpretation methods
- Salience maps of important features are calculated, and they show superpixels that have influenced the prediction most, for example
- To create a map of important pixels, one can repeatedly feed an architecture with several portions of inputs and compare the respective output, or one can visualize them directly by going rearwards through the inverted network from an output of interest;
- Grouped in this category as well is exploiting neural networks with activation atlases through feature inversion. This method can reveal how the network typically represents some concepts
- Considering image or text portions that maximize the activation of interesting neurons or whole layers can lead to the interpretation of the responsible area of individual parts of the architecture.



