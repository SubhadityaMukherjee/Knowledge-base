---
title: Maximum LIkelihood
toc: true
tags:
  - loss
date modified: Tuesday 27th August 2024, Tue
date created: Tuesday 27th August 2024, Tue
---

# Maximum Likelihood
```toc
```
## Effect
- Consider a model $f[x, \phi]$ that computes an output from input $x$.
- Consider the model computes a conditional probability distribution $Pr(Y|x)$ , Y is output
- This encourages each output $y_i$ to have high probability under $Pr(y_{i}|x_{i})$ computed from input $x_{i}$
- ![](Pasted%20image%2020240827214256.webp)
## Computing a distribution over inputs
- Choose a parametric distribution $Pr(y|\theta)$ defined on output domain y. 
- use the network to compute one or more of the parameters $\theta$ of this distribution
- For example, suppose the prediction domain is the set of real numbers, so y ∈ R. Here, we might choose the univariate normal distribution, which is defined on R. This distribution is defined by the mean μ and variance σ2, so θ = {μ,σ^2}. The machine learning model might predict the mean μ, and the variance σ^2 could be treated as an unknown constant.

## [Maximum likelihood criterion](Maximum%20likelihood%20criterion.md)

## [Log likelihood criterion](Log%20likelihood%20criterion.md)

## Minimizing [Log Likelihood Loss](Log%20Likelihood%20Loss.md)
- [Negative Log Likelihood](Negative%20Log%20Likelihood.md)

## Inference
- When we perform inference, we often want a point estimate rather than a distribution, so we return the maximum of the distribution
- ![](Pasted%20image%2020240827215213.webp)