---
toc: true
title: Simple Gradient Descent

tags: ['gradients']
date modified: Monday, October 10th 2022, 2:02:16 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# [Simple Gradient Descent](Simple%20Gradient%20Descent.md)
- ![](../images/Pasted%20image%2020240903123543.png)
- $$\theta = \theta - \eta \cdot \nabla_{\theta} J(\theta)$$
- It starts with some coefficients, sees their cost, and searches for cost value lesser than what it is now.
- It moves towards the lower weight and updates the value of the coefficients.
- The process repeats until the local minimum is reached. A local minimum is a point beyond which it can not proceed.
- The first step computes the gradient of the loss function at the current position. This determines the uphill direction of the loss function. The second step moves a small distance α downhill (hence the negative sign). The parameter α may be fixed (in which case, we call it a learning rate), or we may perform a line search where we try several values of α to find the one that most decreases the loss.

## [LinearRegression](LinearRegression.md) example
- $$ y = f[x, \phi ] = \phi_{0}+ \phi_{1}x$$
- Use [Least squares loss](Least%20squares%20loss.md)
- $$l_{1}= (\phi_{0}+\phi_{1}x_{i}-y_{i})^{2}$$ is the individual contribution to the loss from the ith training example.
- ![](../images/Pasted%20image%2020240903125356.png) 
- ![](../images/Pasted%20image%2020240903125252.png)
- 