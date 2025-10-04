---
tags: ['temp']
toc: true
title: Protein Modeling
date modified: Monday, October 10th 2022, 2:02:19 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# Protein Modeling
- Using [Bayesian](Bayesian.md) models
- Task : Estimate [Probability](Probability.md) mass function(because discrete) for a finite, discrete distribution -> given a histogram from a sample
- Large number of categories and small number of observations
- ![](../images/Pasted%20image%2020220316121901.png)
	- Estimate [Probability](Probability.md) distrib of amino acids in each column in a protein class. 20 dim [PMF](PMF.md) (one for each site)
	- Can be aligned
	- High chances of class not being present in data
		- [MLE](MLE.md) will assign 0 [Probability](Probability.md) to X
		- Wrong decision made for a lot of them that were not in the training set
		- Cannot use
- 20 dim [PMF](PMF.md) for amnio acid distrib : $\theta = (\theta_{1}, … ,\theta_{20})' = (P(X=A), …, P(X=Y))'$
	- count vectors of amino acids found in a given site in training data D
	- Distributed according to [Multinomial Distribution](Multinomial%20Distribution.md) with l = 20

## Using Prior
- 0 probabilities should not occur. $$\mathcal{H} = (\theta_{1}, …, \theta_{20})' \in \mathbb{R}^{20}|\theta_{j} \in (0,1)$$ and $$ \Sigma_{j} \theta_{j}=1$$
	- 19 dim hypervolume
	- Continuous space and so can use [PDF](PDF.md)
	- [Dirichlet Distribution](Dirichlet%20Distribution.md) is used to represent it because parameterized with l = 20
- ![](../images/Pasted%20image%2020220316123546.png)
- $\alpha$s fixed beforehand



