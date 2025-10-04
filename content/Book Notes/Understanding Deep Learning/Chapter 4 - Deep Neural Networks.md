---
title: Chapter 4 - Deep Neural Networks
toc: true
tags:
  - deeplearning
date modified: Tuesday 27th August 2024, Tue
date created: Tuesday 27th August 2024, Tue
---

# Chapter 4 - Deep Neural Networks
```toc
```
## Intro
- Deep networks : more than one hidden layer
- Both deep and shallow describe piecewise linear mappings from input -> output
- A shallow network can describe complex functions but might have too many hidden layers to be practically possible to use.

### Why did deep learning take off
- Krizhevsky et al. (2012) aka [ImageNet](../../KB/ImageNet.md)
- Larger datasets
- Improved processing power for training
- [Relu](../../KB/Relu.md)
- [SGD](../../KB/SGD.md)

## Composing networks
- [Composing shallow neural networks to get deep networks](../../KB/Composing%20shallow%20neural%20networks%20to%20get%20deep%20networks.md)
## General deep neural networks
- Consider a deep network with 2 hidden layers, each of which has 3 hidden units
	- ![[Pasted image 20240827203741.png]]
	- ![[Pasted image 20240827203801.png]]
	  
## How does the network deal with complicated functions?
- ![[Pasted image 20240827203949.png]]
## Hyperparameters
- Capacity : total number of hidden units 
- NNs represent a family of families of functions relating input to output
### Width
- Number of hidden units in each layer ($D_{1}, D_{2},..., D_{K}$)
### Depth
- Number of hidden layers ($K$)

## Matrix notation to represent deep networks
- [Matrix notation for NNs](../../KB/Matrix%20notation%20for%20NNs.md)

## Shallow vs deep networks
- [Shallow vs deep networks](../../KB/Shallow%20vs%20deep%20networks.md)

## Other notes
- [Universal Approximation Theorem](../../KB/Universal%20Approximation%20Theorem.md)
- [Depth Efficiency of Neural Networks](../../KB/Depth%20Efficiency%20of%20Neural%20Networks.md)
- [Width Efficiency of Neural Networks](../../KB/Width%20Efficiency%20of%20Neural%20Networks.md)
