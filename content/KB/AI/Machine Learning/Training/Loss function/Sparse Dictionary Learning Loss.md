---
toc: true
title: Sparse Dict Learning Loss
tags: ['loss']
date modified: Monday, October 10th 2022, 2:02:16 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# Sparse Dict Learning [loss](../Tag%20Pages/loss.md)
- $$L(X) = n^{-1}\Sigma_i^n ||x_i - Dr_i ||^2 + \lambda \Sigma_i |r_i|$
- $\lambda \Sigma_i |r_i|$ is Lasso/L1 [Lp Regularization](Lp%20Regularization.md)
- Predictions : $r = argmin_r ||x- Dr_i ||^2 + \lambda \Sigma_i |r_i|$



