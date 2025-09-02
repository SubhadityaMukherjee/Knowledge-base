---
tags: ['temp']
toc: true
title: Bayesian Prior
date modified: Monday, October 10th 2022, 2:02:33 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# [[Bayesian]] Prior
- Use prior knowledge as beliefs (param vectors $\theta$). Cast in the form of a [[Probability]] distribution over the space $\Theta$ .
	- Weak knowledge most times
	- For a K parametric [[PDF]] $p_{x}$ , $\Theta \in \mathbb{R}^{K}$ .
	- Not connected to Random variable(RVS).
	- Does not model outcomes. Instead has "beliefs" about true distribution $P_{X_{i}}$
	- Each $\theta \in \mathbb{R}^{K}$ corresponds to one specific [[PDF]] $p_{X}(\theta)$ -> single candidate distribution $\hat P_{X}$ for values $x_i$ (In frequentist, it models single data points)
	- Since this is a distribution over [[Distributions]], it is a hyperdistribution
	- N dim [[PDF]] $p_{\otimes}x_{i}: \mathbb{R}^{N} \rightarrow \mathbb{R}^{\geq 0}$ for the distribution of $RV \otimes_{i}X_{i}$
		- $p_{\otimes_{i}}x_{i}((x_{i},…, x_{N})) = p_{x_{1}}, …, p_{x_{N}}(x_{N}) = \Pi_{i}p_{X}(x_{i})$
		- $p_{\otimes_{i}}x(D|\theta)$ -> [[PDF]] values on a data sample D $p_{\otimes_{i}}x_{i}((x_{i},…, x_{N})) = p_{\otimes_{i}}(\theta)(D)$
	- When $\theta$ is fixed then $p_{\otimes_{i}}x(D|\theta)$ is a function of data vectors D. For each sample, it describes how probable this distribution is assuming the true distribution of X is $p_{X}(\theta)$
	- When D is fixed, then it is a function of $\theta$. But this does not really measure anything.
		- Integral over $\theta$ is not 1
		- It is a function of $\theta$ and so it is a likelihood function. [[MLE]]
		- If given data D -> it can show which models are more likely than others.
		- Higher values of	$p_{\otimes_{i}}x(D|\theta)$ are better



