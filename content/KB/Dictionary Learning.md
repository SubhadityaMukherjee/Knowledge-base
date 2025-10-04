---
tags: ['temp']
toc: true
title: Dictionary Learning
date modified: Monday, October 10th 2022, 2:02:29 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# Dictionary Learning
- Given : N unlabeled data points $$x_i \in \mathcal{R}^d$$
- To find:
	- Linear rep of these points based on set of basis vectors
		- $$x = \Sigma_i^k r_i \cdot d_i = Dr$$
		- dimension d
		- r are repr weights corresponding to basis vector d
		- D is a dict with basis vectors
		- R contains weights. Scalar
		- $$||d_i|| \leq 1$
- [Sparse Dictionary Learning Loss](Sparse%20Dictionary%20Learning%20Loss.md)
- After learning, these can be used as discriminative [Features](Features.md)
	- Expensive to compute



