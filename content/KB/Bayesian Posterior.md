---
tags: ['temp']
toc: true
title: Bayesian Posterior
date modified: Monday, October 10th 2022, 2:02:33 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# [Bayesian](Bayesian.md) Posterior
- When D is fixed though, this becomes a function of Model Candidates
- Non negative on K dim param space
- Not a [PDF](PDF.md) but if we divide it by its integral -> [PDF](PDF.md) .
	- $$\frac{p_{\otimes_{i}}x(D|\theta)h(\theta)}{\int_{\mathbb{R}^K}p_{\otimes_{i}}x(D|\theta)h(\theta)d\theta}$$
	- Prob distrib over candidate models
- If the denominator is replaced written as $p(D)$ then it looks like the [Bayes Rule](Bayes%20Rule.md)
- Shape : $P(D|\theta)h(\theta)$
	- Integral not 1
	- [Proto Distributions](Proto%20Distributions.md) on $\theta$ space



