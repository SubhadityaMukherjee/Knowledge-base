---
toc: true
title: Normal Distribution
tags: ['distributions']
date modified: Monday, October 10th 2022, 2:02:21 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# Normal Distribution
- $$Pr(y|\mu, \sigma^{2}) = \frac{1}{\sqrt{2\pi\sigma}}e^{-\frac{(y-\mu)^{2}}{2\sigma^{2}}}$$
- Mean $\mu$ and std $\sigma$. $\mu$ is max and $\mu \pm \sigma$ is locations of zeros of second derivative
- ![](../images/Pasted%20image%2020220319144034.png)
- $\mathcal{N}(0,1)$
- [Central Limit Theorem](Central%20Limit%20Theorem.md)

## Properties
- Linear combinations of normal distributed independant RVs are normal distributed
- X,Y have means $\mu$ and v and variances $\sigma^{2}$ and $\tau^{2}$. Then $aX + bY$ is normally distributed and has mean : $a\mu + bv$ and variance $\alpha^{2}\sigma^{2}+b^{2}\tau^{2}$

## Computing the Value
- $$\int_{a}^{b} \frac{1}{\sqrt{2\pi\sigma}}e^{-\frac{(x-\mu)^{2}}{2\sigma^{2}}}dx$$
- Transform $\mathscr{N}(\mu, \sigma^{2})$ to $\mathscr{N}(0,1)$
- $$Z = \frac{X-\mu}{\sigma}$$
- $$\int_{\frac{a-\mu}{\sigma}}^{\frac{b-\mu}{\sigma}}\frac{1}{\sqrt{2\pi}}e^{-\frac{(x)^{2}}{2}}dx$$
- Compute by using Cumulative [Density](Density.md) function $\phi$
- Iterative solvers
- $$\phi(\frac{b-\mu}{\sigma})-\phi(\frac{a-\mu}{\sigma})$$
- $$\hat \mu = \frac{1}{N}\Sigma_{i}(x_{i})$$ $$\hat \sigma^{2}= \frac{1}{N-1}\Sigma_{i}(x_{i}-\hat\mu)^2$$



