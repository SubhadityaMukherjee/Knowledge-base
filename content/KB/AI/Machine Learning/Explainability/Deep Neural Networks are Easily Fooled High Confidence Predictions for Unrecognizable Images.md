---
toc: true
title: Deep Neural Networks are Easily Fooled High Confidence Predictions for Unrecognizable Images

tags: ['explainability']
date modified: Monday 27th March 2023, Mon
date created: Monday 27th March 2023, Mon
---

# Deep Neural Networks Are Easily Fooled High Confidence Predictions for Unrecognizable Images


- @nguyenDeepNeuralNetworks2015
- Current study
	- False positives
	- MAP Elites algorithm 
	- parallel generation
	- Direct encodings
	- Indirect encodings
	- Gradient ascent generation

## GA
- Population of individuals 
- Each individual has a fitness 
- Mutation makes small edits to specific individuals 
- Recombination (not used here)

## Direct Encoding
- Individuals are images in pixel space 
- Fitness is the confidence of the DNN that the individual is a class 
- Mutations make edits to the pixel values

## Indirect Encoding
- Individuals are Compositional Pattern-Producing Networks (CPPNs) 
- The CPPN generates an image 
- All individuals initially have no hidden neurons 
- Mutations add new neurons to the networks
- Maximize confidence of the network

## Gradient Ascent
- Take the gradient with respect to the image pixel values 
- Modify the image by moving it in the direction of the gradient

## MNIST Results - EAs
- ![](../images/Pasted%20image%2020230327124348.png)

## ImageNet Results - EAs
- Harder to fool
- Different runs result into differences in patterns
- Removing repetitive patterns does not cause a dramatic confidence drop
- Global structures are not learned
- ![](../images/Pasted%20image%2020230327124359.png)
- ![](../images/Pasted%20image%2020230327124413.png)
- ![](../images/Pasted%20image%2020230327124421.png)

## What about a Fooling Class?
- MNIST
	- Added an 11th fooling class. 
	- Evolved unrecognizable images were still recognized as digits. 
	- Number of misclassifications did not decrease.
- ImageNet
	- Added an 1001st fooling class. 
	- No decrease in confidence for directly evolved images, but already low confidence. 
	- Confidence decreased from 88.1% to 11.7% for indirectly evolved images.
- Indirectly evolved images are easier to differentiate.

## Gradient Ascent Results
- Maximize softmax output
- Produced unrecognizable images classified with 99.99% confidence



