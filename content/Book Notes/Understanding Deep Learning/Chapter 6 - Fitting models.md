---
title: Chapter 6 - Fitting models
toc: true
tags:
  - optimizer
  - loss
date modified: Tuesday 3rd September 2024, Tue
date created: Tuesday 3rd September 2024, Tue
---

# Chapter 6 - Fitting Models
```toc
```
- Minimizing [loss](../../Tag%20Pages/loss.md) , [Chapter 5 - Loss functions](Chapter%205%20-%20Loss%20functions.md)
- basic : compute the derivatives of the gradients of the loss wrt params and then adjust the params based on gradients : decrease [loss](../../Tag%20Pages/loss.md)

- Goal is to minimize the loss $$\hat \phi= \underset {\phi}{argmin}[L[\phi]]$$
## [Gradient Descent](../../KB/Gradient%20Descent.md)
## [[Gabor Model]]

- Local minima and [Saddle Points](../../KB/Saddle%20Points.md)
- [SGD](../../KB/SGD.md)
- [SGD Momentum](../../KB/SGD%20Momentum.md)
- [Nesterov Momentum](../../KB/Nesterov%20Momentum.md)
- [Adam](../../KB/Adam.md)
- [Adagrad](../../KB/Adagrad.md)
- [Rmsprop](../../KB/Rmsprop.md)
- [AdaDelta](../../KB/AdaDelta.md)
- [Amsgrad](../../KB/Amsgrad.md)
- [Learning Rate Warmup](../../KB/Learning%20Rate%20Warmup.md)
- [Learning Rate Scheduling](../../KB/Learning%20Rate%20Scheduling.md)

## Useful Links
- [bag of tricks for computer vision](https://arxiv.org/abs/1812.01187)
- [visualizing optimisers 1 ](https://emiliendupont.github.io/2018/01/24/optimization-visualization/)
- [optimizers but easier and less scary math](https://fastai.github.io/fastbook2e/accel_sgd.html)
- [gradient descent video](https://www.youtube.com/watch?v=IHZwWFHWa-w)
- [backprop video](https://www.youtube.com/watch?v=Ilg3gGewQ5U)
- [very advanced blog on if neural networks are overfitted](https://lilianweng.github.io/posts/2019-03-14-overfit/)
- [1cycle scheduling and warmup](https://www.deepspeed.ai/tutorials/one-cycle/)
- [Automatic differentiation](https://huggingface.co/blog/andmholm/what-is-automatic-differentiation)

## Qs
- Why do we need to modify the learning rate while training?
- How would you decide a learning rate depending on batch size?
- What optimizer would you use for inference?