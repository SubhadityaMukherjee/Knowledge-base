---
title: Phase Transition Model Zoo
toc: true
tags:
  - conference
date modified: Wednesday 27th November 2024, Wed
date created: Wednesday 27th November 2024, Wed
---

# Phase Transition Model Zoo
```toc
```
- konstantin schurholt
- [[Transfer Learning]], model averaging, scaling models does not always work

## Phase Transition in Physical Systems
- ![[c3f5b449f54cd092dbda52d3bf77e953_MD5.webp]]
- between phases is an interpolation
- order params with some control params
	- eg : temp and pressure in water
- are there phases in NN?

## Regimes in NN
- [[Double Descent]]
- [[Gradient Descent]]
- Scaling loss : kaplan et al.20
- transitions between regimes can be sharp or smooth
- [[Understanding deep learning still requires rethinking generalization]]

## Statistical Mechanics
- eg : [[Hopfield networks]] , [[Perceptron]], [[tree parity machine]]

## Control Params in NN
- temperature and load are relative
### Temp
- ![[24159c159523a80531aaea4a458c8970_MD5.webp]]

### Load
- ![[681678457690bbf9c05c0a553dad643f_MD5.webp]]

## Emperical Phases in NN Performance
- ![[a8ad6f8a6fee1e988e7a7420d651a35d_MD5.webp]]
- taxonomizing local vs global
	- https://proceedings.neurips.cc/paper/2021/hash/9b72e31dac81715466cd580a448cf823-Abstract.html 
- expected phases emerge on the load temperature landscape
- load : complexity/capactity
- temperature : noisiness of training
- 5 phases, phase IV-B is the best
- ~5k models trained from scratch
- hessian : minima
	- flatness of the minima
		- flatter minima generalizes better : depending on where you are
	- ![[ddc94bc612244ce7c57afc673202e016_MD5.webp]]
- mode connectivity
	- ![[63e2a7b78050f423fbdd8a338a2f67bd_MD5.webp]]
	- models trained with same config + different seed
	- if so, find a path where the loss is the same
	- ![[15852d97d20561a65bf24d8d6e683304_MD5.webp]]
- ![[385d0acd9be3620e8696725aebc10161_MD5.webp]]
## Phase Transition in Model Zoo
- phase transitions are a general phenomenon in NNs
- ![[ab59d3e9b2f3cc11cc50531fd6f01e38_MD5.webp]]
- all of these requires datasets of models that cover phase transitions
- since temp/load are basically have the same effects, didnt train every possibility
- ![[f6d4ea2b0607345f730552449ac675cc_MD5.webp]]
	- [[Vision Transformer]] are very different
		- big optimal phase
		- for [[CIFAR]], bad performance without data augmentation
			- (could also be because the dataset has a lot of noise)
- ![[e3daf7ed9807d817abc5457c98c86c69_MD5.webp]]

## Applications
- research on transitions
	- might identify root causes for performance
	- ![[6f8525b8dbdf04655801d8cc39d77855_MD5.webp]]
	- ![[54db6dae3c29b2666398a9b1d84e81f8_MD5.webp]]
	- ![[83e4bbd9fe6052daaf5e098394009796_MD5.webp]]