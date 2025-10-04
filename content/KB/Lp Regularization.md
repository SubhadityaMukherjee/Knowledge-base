---
toc: true
title: Lp Regularization
tags: ['regularization']
date modified: Monday, October 10th 2022, 2:02:23 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# Lp Regularization
- Tikhonov
- Penalty considering weights
- ![](../images/Pasted%20image%2020240918105448.png)
- $$L^\ast(\theta) = L(\theta) + \lambda \Sigma_i |\theta_i|^p$$
- [Frobenius norm](Frobenius%20norm.md)
- Weight Decay
- p = 2
- Encourages optimization [Trajectory](Trajectory.md) perpendicular to isocurves
- ![](../images/Pasted%20image%2020220306133032.png)
- Tune $\lambda$
- Lasso
	- p = 1
	- Sparse
	- With linear model : feature selection
- Grid search : log scale
- Too large : underfit, too small : overfit
- [Cross Validation](Cross%20Validation.md) required



