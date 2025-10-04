---
tags: ['temp']
toc: true
title: Fitting
date modified: Monday, October 10th 2022, 2:02:27 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# Fitting
- Bayes risk
	- Minimal expected risk over set of all functions $$R_B = min_{f\in y^X} R(f)$$
	- If minimized -> Best possible function
	- Capacity of hypothesis space $\mathcal{H}$
	- It is essentally all possible things. In reg, all possible affine linear fns. In neural networks, all possible specific connection structure.
		- If low, $$\mathscr{F} = R(f) - R_B$$ is large : Underfitting (Huge difference between best risk and current risk)
		- If high, $$\mathscr{F} = R(f) - R_B$$ is small : Overfitting (Tiny difference between best risk and current risk)



