---
toc: true
title: Window Based Regression
tags: ['architecture']
date modified: Monday, October 10th 2022, 2:02:13 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# Window Based Regression
- [TIme Series](TIme%20Series.md)
- input window : $$u(t-d+1), u(t-d+2), …. , u(t-1) , u(t)$$
- Require regression function $$f:(\mathbb{R}^k)^d \rightarrow \mathbb{R}^m$$
	- $$k \times d$$ dim matrix
	- Flatten into $$d \cdot k$$ vector and apply [Quadratic Loss](Quadratic%20Loss.md)

## Non Linearity
- Add fixed nonlinear transforms to input arguments : eg polynomials
- [Volterra expansion](Volterra%20expansion.md)



