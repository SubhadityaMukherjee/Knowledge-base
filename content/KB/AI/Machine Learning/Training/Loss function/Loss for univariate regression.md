---
title: Loss for univariate regression
toc: true
tags:
  - loss
date modified: Wednesday 28th August 2024, Wed
date created: Wednesday 28th August 2024, Wed
---

# Loss for univariate regression
```toc
```
- Predict a single scalar output $y \in \mathbb{R}$
- Use univariate [Normal Distribution](Normal%20Distribution.md) 
	- ![](Pasted%20image%2020240828095716.webp)
- ![](Pasted%20image%2020240828095740.webp)
- ![](Pasted%20image%2020240828095747.webp)
- Find parameters $\hat \phi$ that minimize $L[\phi]$\
- [Least squares loss](Least%20squares%20loss.md)

## Inference
- Predict the mean $\mu = f[x, \phi]$ of the [Normal Distribution](Normal%20Distribution.md) over y
- We find the single best point estimate $\hat y$ and we take max of the predicted distribution $$\hat y = \underset{y}{argmax}[Pr(y|f|x, \hat \phi, \sigma^{2})] = f[x, \hat \phi]$$
### Estimating if variance constant everywhere
- [Homoscedatic](Homoscedatic.md)
- Since the equation does not depend on variance, we pretend $\sigma^{2}$ is a learned parameter and minimize it wrt $\phi, \sigma^{2}$
- ![](Pasted%20image%2020240828100529.webp)
- ![](Pasted%20image%2020240828100420.webp)
  
### Estimating if variance is not constant
- [Heteroscedatic](Heteroscedatic.md) 
- Train a network that computes both mean and variance
- Variance should be positive, but the result of composing networks might not be. To make it, pass it through the squaring function
- ![](Pasted%20image%2020240828100835.webp)

### [Homoscedatic](Homoscedatic.md) vs [Heteroscedatic](Heteroscedatic.md) Regression
- ![](Pasted%20image%2020240828100938.webp)
