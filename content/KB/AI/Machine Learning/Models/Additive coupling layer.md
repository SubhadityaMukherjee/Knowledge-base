---
title: Additive coupling layer
toc: true
tags:
  - distributions
  - architecture
date modified: Tuesday 19th November 2024, Tue
date created: Tuesday 19th November 2024, Tue
---

# Additive Coupling Layer
```toc
```
- $$g(z_{d+1:D}; m(z_{1:d})) = z_{d+1:D}+ m(z_{1:d})$$
- So no matter what m is , maybe a neural network, it is still possible to invert it and compute whatever we need
- They have a unit jacobian determinant, so neither contract nor expand space
	- preserves volume
	- but we don't really want this because we want the model to be able to freely scale the amount of latent space it uses
	- So we use a [[Scaling matrix for coupling layers]]