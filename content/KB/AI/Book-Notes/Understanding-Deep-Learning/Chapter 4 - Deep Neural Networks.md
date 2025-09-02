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
- Krizhevsky et al. (2012) aka [[ImageNet]]
- Larger datasets
- Improved processing power for training
- [[Relu]]
- [[SGD]]

## Composing networks
- [[Composing shallow neural networks to get deep networks]]
## General deep neural networks
- Consider a deep network with 2 hidden layers, each of which has 3 hidden units
	- ![[Pasted image 20240827203741.webp]]
	- ![[Pasted image 20240827203801.webp]]
	  
## How does the network deal with complicated functions?
- ![[Pasted image 20240827203949.webp]]
## Hyperparameters
- Capacity : total number of hidden units 
- NNs represent a family of families of functions relating input to output
### Width
- Number of hidden units in each layer ($D_{1}, D_{2},..., D_{K}$)
### Depth
- Number of hidden layers ($K$)

## Matrix notation to represent deep networks
- [[Matrix notation for NNs]]

## Shallow vs deep networks
- [[Shallow vs deep networks]]

## Other notes
- [[Universal Approximation Theorem]]
- [[Depth Efficiency of Neural Networks]]
- [[Width Efficiency of Neural Networks]]
