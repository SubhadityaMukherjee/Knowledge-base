---
title: Recipe for constructing loss functions
toc: true
tags:
  - loss
  - deeplearning
date modified: Wednesday 28th August 2024, Wed
date created: Wednesday 28th August 2024, Wed
---

# Recipe for constructing loss functions
```toc
```
- Using [Maximum Likelihood](Maximum%20Likelihood.md)
- For training data ${x_{i}, y_{i}}$
	- Choose a probability distribution $Pr{y|\theta}$ defined over the domain of the predictions y with distribution parameters $\theta$
	- Choose an ML model $f|x, \phi|$ where $\theta = f|x, \phi|$ and $Pr(y|\theta) = Pr(y|f|x, \phi|)$ 
	- Training -> Find the parameters $\phi$ that minimize the [Negative Log Likelihood](Negative%20Log%20Likelihood.md) over the training data ${x_{i}, y_{i}}$ 
	- Inference -> Either return $Pr(y|f[x, \hat \phi])$ or the value where this distribution is minimized
- If data is differently distributed and there is no loss associated, just transform the distribution beforehand