---
title: Probabilistic circuits
toc: true
tags:
  - talk
date modified: Thursday 20th February 2025, Thu
date created: Thursday 20th February 2025, Thu
---

# Probabilistic Circuits
```toc
```
- Gennaro Gala
## Intro
- should be tractable
- probablistic generative models
- tractable s expressive
- overparameterization
- imposing structure
- [[Probabilistic Circuit Units]]

## Why Generative
- can be sampled from top to bottom

## Why Use Probabilistic Circuits
- "language of circuits"
- they can turn Knowledge graph embedding models into generative models
- sample triples
- can speed up inference in multi token predictions
	- einsum
	- sampling k next tokens, each have no relationship with each other
		- tensor factorization can help with that by outputting the weights instead
## Tensor Decomposition
- probabilistic modesl can be tensorsized 
- sequence of [[Einsum]]
- so each layer units can be parallely computed
- Tucker layer
- folds
	- how many of the same layer are stacked together
## Training
- tesors parameterized the model
- if we can solve integrals, comput c(X)
	- or apply numerical quadrature

## Probabilistic Integral Circuits
- new unit - integral unit [[Probabilistic Circuit Units#Types]]
- numerical quadrature
- [[VAE]] as intractable PICs
- neural PICS
	- discretize tensors (?)
	- train EBM and decoders parameterizing the PIC
	- on query - get tensors parameteriaing QPC
	- hyper network approach
	- expensive I guess
- QPC > PC usually
## Neural Functional Sharing