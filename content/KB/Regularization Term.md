---
toc: true
title: Term
tags: ['regularization']
date modified: Monday, October 10th 2022, 2:02:18 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# Term
- Penalty term
- Cost function that penalizes model params $\theta$ with a high degree of flexibility
- $$h_{opt} = argmin_{h \in \mathcal{H}} \frac{1}{N}\Sigma_{i=1}^N L(h(x_i), y_i)+ \alpha^{2}R(\theta_h)$$
- $\alpha^2$ determines how much regularizer affects the model
	- Larger : soft models
	- Increasing -> Down regulating flexibility
	- 0 = overfitting and unregularized risk
	- $\infty$ does not care about training data at all. Only cares about minimal penalty
		- Dead model

## Types
- [Lp Regularization](Lp%20Regularization.md) for p =2
	- Soft models
	- Squared sum of model params



