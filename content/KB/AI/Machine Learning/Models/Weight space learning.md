---
title: Weight space learning
toc: true
tags:
  - conference
  - representationlearning
date modified: Wednesday 20th November 2024, Wed
date created: Wednesday 20th November 2024, Wed
---

# Weight Space Learning
```toc
```
- Damian Borth, st.gallen
	- [paper](https://arxiv.org/pdf/2406.09997)
- treat weights as data points - representation learning
- can we look at networks -> infer the latent factors from the weights?
- is there knowledge inside models, but can be accessed when they are frozen?
- [[Capsule Network#Loss|loss]] surfaces and optimization problem of NN are non-convex
- nn training optimization is very high dimensional
- what is the relationship between the characterstics(behavior, performance etc) and their solution in weight space
- GDPR : linked model to database
- Hypothesis
	- nn populate a structure in weight space
	- structure contains info on properties and generating factors of the models
- [[Autoencoders with Convolutions#Encoder|Encoder]] [[Autoencoders with Convolutions#Decoder|Decoder]] [[architecture]] for weight vectors
	- then on to down-stream tasks
- rather huge model zoo generated
	- variated [[Chapter 4 - Deep Neural Networks#Hyperparameters|hyperparameters]] with [[Dropout#Dropout|Dropout]]
	- magnitude [[Pruning]]
	- two types of pre-training : supervised, [[Contrastive Loss|contrastive]]
- weight space is symmetric sometimes : ACG [[architecture]]
	- multiple versions of NN which do the same thing -> can be used to reach them from a space
- [[Contrastive Loss|contrastive]] loss
- linear heads are fitted on the model zoos validation split
	- encoder is frozen
- [[Initialization#Initialization|initialization]]
	- random normal
	- glorot
	- [[Orthogonal Initialization#Orthogonal Initialization|orthogonal]]
	- he normal
	- truncated normal
- train and test on [[MNIST]] ,[[Fashion MNIST]] , [[CIFAR]] , [[SVHN]]
- hypernetworks dont really work somehow?
- train a encoder decoder transformer 
	- one forward pass destroys models
	- took the weight vector and calculated MSE
		- layers that occupy more are re-constructed better (higher mean)
		- also what was apparently needed for [[Stable Difusion]]
		- paper : [[Taming Transformers for high res image synthesis]]
			- perception loss + [[GAN]]
- sample space
	- are they just sampling the train set? - some ablation done to prove it's not lol
- [[Sequential auto encoding of neural embeddings - SANE]]