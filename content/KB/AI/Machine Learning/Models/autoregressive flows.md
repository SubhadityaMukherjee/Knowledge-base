---
title: autoregressive flows
toc: true
tags:
  - architecture
date modified: Tuesday 19th November 2024, Tue
date created: Tuesday 19th November 2024, Tue
---

# Autoregressive Flows
```toc
```
- ![[c2edff490cf80bba6f98164821c7f513_MD5.webp]]
- use them as normalizing flows
- a model that sequentially samples each pixel on an image, wrt the previous pixel in a fixed order
- consider the conditional densities as gaussians
	- From [[MADE - Masked autoencoder for distribution estimation]] and [[Masked autoregressive flow for density estimation]], 
		- the sampling noise at each step can be used as a latent variable
		- $$p_\theta(x_{1}, x_{2}, … , x_{n}) = \Pi_{i}^{n}p_\theta(x_{i} \vert x_{<i})$$
		- $\mu_{i}= f_\mu(x_{<i})$ and $log \sigma_{i}= f_\sigma(x_{<i})$
		- the latent factor = $z_{i} \sim N(0,1)$ 
		- observed -> $x_{i}= \mu_{i}+ z_{i}\exp(\log \sigma_{i})$ 
	- Since these are sequentially sampled, we can't parallelize them. Instead from [[Improved variational inference with inverse autoregressive flows]] we can use [[inverse autoregressive flows]]