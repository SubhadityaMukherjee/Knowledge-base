---
tags: ['temp']
toc: true
title: Emperical Risk
date modified: Monday, October 10th 2022, 2:02:28 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# Emperical Risk
- TRAINING ERROR. Mean loss computed over training examples
- $$R(f) = \mathbb{E} _{(X,Y) \sim P(X,Y)}[l(y, f(x))]$$
- $$R^{emp}(h) = \frac{1}{N}\Sigma_{i=1}^{N}L(h(x_{i}), y_{i})$$
- joint prob distribution $P(X\in A,Y=c)$ is unknown
	- [Decision Boundaries](Decision%20Boundaries.md)
	
- Learning set $$\mathcal L$$ is finite
- Need an estimator to evaluate it
	- Supervised Learning
		- Compute $$\mathcal L_{train}$$
		- Risk train = (1/M)(sum of loss values for (y, f(x)))
		- This is an unbiased estimator, so we can use it to approximate the optimal function f* that minimizes $$\mathbb{R}$$
		- This means that we find $$argmin_{f\in F} \hat R(f, \mathcal{L}_Train)$$ (out of all the possible functions)
		- $$lim_{M\rightarrow \infty}(f^*_{\mathcal{L}_Train}) = f^*$$ : converges to the fn that minimizes emprical risk
	- Ordinary least squares regression



