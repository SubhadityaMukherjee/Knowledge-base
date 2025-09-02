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
- A large list of useful loss functions can be found [[loss]]
- A large list of useful distributions can be found here [[Distributions]]
- A loss function or cost function L[φ] returns a single number that describes the mismatch between the model predictions f[xi, φ] and their corresponding ground-truth outputs $y_i$

## Distributions
- ![[Pasted image 20240828112456.webp]]

## Maximum Likelihood
### [[Log Likelihood Loss]]
### [[Maximum Likelihood]]

## Constructing New Loss Functions
### [[Recipe for constructing loss functions]]

### [[Loss for univariate regression]]

### [[Loss for binary classification]]

### [[Loss for multiclass classification]]

- Difference between the distributions : [[KL Divergence]] or [[Cross Entropy]]

### For Multimodal
- Fusion loss
- Multiple attention heads : backprop from heads
## Other Notes
- [[heteroscedastic nonlinear regression]]
- [[Robust regression]]
- [[Quantile Regression]]
- [[Focal Loss]]
- [[Van Mises distribution]]
- Non probabilistic approaches - [[Hinge Loss]], [[AdaBoost]]

## Useful Links
- [visualizing loss functions](https://www.kaggle.com/code/mayank1101sharma/visualizing-loss-functions)
- [visualizing the loss landscape - neurips](https://proceedings.neurips.cc/paper_files/paper/2018/file/a41b3bb3e6b050b6c9067c67f663b915-Paper.pdf)
- [distributions -> loss functions](https://mindfulmodeler.substack.com/p/bridging-the-gap-from-statistical)