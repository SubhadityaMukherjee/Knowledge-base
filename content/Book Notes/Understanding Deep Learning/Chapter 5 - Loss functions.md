---
title: Chapter 5 - Loss functions
toc: true
tags:
  - deeplearning
  - loss
date modified: Tuesday 27th August 2024, Tue
date created: Tuesday 27th August 2024, Tue
---

# Chapter 5 - Loss Functions
```toc
```
- A large list of useful loss functions can be found [loss](../../Tag%20Pages/loss.md)
- A large list of useful distributions can be found here [Distributions](../../KB/Distributions.md)
- A loss function or cost function L[φ] returns a single number that describes the mismatch between the model predictions f[xi, φ] and their corresponding ground-truth outputs $y_i$

## Distributions
- ![[Pasted image 20240828112456.png]]

## Maximum Likelihood
### [Log Likelihood Loss](../../KB/Log%20Likelihood%20Loss.md)
### [Maximum Likelihood](../../KB/Maximum%20Likelihood.md)

## Constructing New Loss Functions
### [Recipe for constructing loss functions](../../KB/Recipe%20for%20constructing%20loss%20functions.md)

### [Loss for univariate regression](../../KB/Loss%20for%20univariate%20regression.md)

### [Loss for binary classification](../../KB/Loss%20for%20binary%20classification.md)

### [Loss for multiclass classification](../../KB/Loss%20for%20multiclass%20classification.md)

- Difference between the distributions : [KL Divergence](../../KB/KL%20Divergence.md) or [Cross Entropy](../../KB/Cross%20Entropy.md)

### For Multimodal
- Fusion loss
- Multiple attention heads : backprop from heads
## Other Notes
- [heteroscedastic nonlinear regression](../../KB/heteroscedastic%20nonlinear%20regression.md)
- [Robust regression](../../KB/Robust%20regression.md)
- [Quantile Regression](../../KB/Quantile%20Regression.md)
- [Focal Loss](../../KB/Focal%20Loss.md)
- [Van Mises distribution](../../KB/Van%20Mises%20distribution.md)
- Non probabilistic approaches - [Hinge Loss](../../KB/Hinge%20Loss.md), [[AdaBoost]]

## Useful Links
- [visualizing loss functions](https://www.kaggle.com/code/mayank1101sharma/visualizing-loss-functions)
- [visualizing the loss landscape - neurips](https://proceedings.neurips.cc/paper_files/paper/2018/file/a41b3bb3e6b050b6c9067c67f663b915-Paper.pdf)
- [distributions -> loss functions](https://mindfulmodeler.substack.com/p/bridging-the-gap-from-statistical)