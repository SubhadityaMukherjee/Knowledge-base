---
title: The Unified Causal AI Pipeline
toc: true
tags:
  - casual
  - talk
date modified: Friday 8th November 2024, Fri
date created: Friday 8th November 2024, Fri
---

# The Unified [[Causality#Causality|Causal]] AI Pipeline
```toc
```
- Sara Magliacana - prof at UvA

## Intro
- predict the effect of actions and decide effective policies - and how
- dl - can learn representations from unstructured data
- predict effects of interventions
	- causal variables not observed directly
	- no labels
	- just high level observations
- tasks
	- identify causal variables from observations
	- learn causal relations between them

## Recovering Causal Variables
- theoretical guarantees
- without supervision, cannot identify exact causal variables - but up to equivalence class (aka not perfectly)
	- somehow seems like trying to recover some variables from a tangled mess of the ground truth
	- 1-1 map? 

## Dynamic Bayesian Networks
- [[Markov Chain]]
- stationarity : transition model (edge) are same across pairs of time steps
- no instantaneous effects : no edges between vars at same timestep
- extension of [[Bayesian]] networks
- environment : AI Tutor

## [[TemporalLearning#Temporal Learning|Temporal]] Intervened Sequences
- learn underlying causal process from temporal seq of high dim data (images) ${X^{t}}^{T}_{t-1}$
- Assume latent causal process in Dynamic Bayesian Networks with K multidim causal variables 
- Assume interventions can happen, observe binary targets $I^{t}_{i}$ and $I_{i} \rightarrow C_{i}$ 
- targets are 1-1 with causal variables
- model with latent variable
- paper : [CITRIS](https://proceedings.mlr.press/v162/lippe22a.html) (phillip lippe, sara magliacane)
	- stochastic intervention : we dont know where the ball will be
	- simplified identification proof
	- minimal causal variables
		- part of the variable that is varying
		- identify them up to invertible component wise transforms if $I_{i}^{t}$ up to $I_{j}^{t}$
	- CITRIS - [[VAE]]
		- cant really use pretrained autoencoder since you assume its disentangling
	- normalizing flows : CITRIS NF
		- use a pretrained autoencoder
- BISCUIT - causal representation learning from binary interactions
	- extension of TRIS
	- effect encoded in binary interaction variables
	- assume action has to affect causal variables in a binary way
	- More BISCUIT - VAE and NF
- Environments - CausalWorld, iTHOR
- dynamic interaction map
- CRL World models

## Why
- causal representation learning
- causal discovery
- inspired ml/rl research
- explainable ai
- causal effect estimation

## Future
- BISCUIT + DAFT RL