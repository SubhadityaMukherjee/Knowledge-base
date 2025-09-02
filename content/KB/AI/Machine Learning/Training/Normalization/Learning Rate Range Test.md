---
toc: true
title: Learning Rate Range Test

tags: ['regularization']
date modified: Monday, October 10th 2022, 2:02:24 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# Learning Rate Range Test
- Smith, LN (2018) [A disciplined approach to neural network hyper-parameters: Part 1--learning rate, batch size, momentum, and weight decay](https://arxiv.org/abs/1803.09820) arXiv preprint arXiv:1803.09820
- It is relatively straight-forward: in a test run, one starts with a very small learning rate, for which one runs the model and computes the loss on the validation data. One does this iteratively, while increasing the learning rate exponentially in parallel. One can then plot their findings into a diagram representing loss at the y axis and the learning rate at the x axis. The x value representing the lowest y value, i.e. the lowest loss, represents the optimal learning rate for the training data.
- The learning rate at this extrema is the largest value that can be used as the learning rate for the maximum bound with cyclical learning rates but a smaller value will be necessary when choosing a constant learning rate or the network will not begin to converge.
- Smoothed loss changes

```
for i in range(moving_average, len(learning_rates)):
    loss_changes.append((losses[i] - losses[i - moving_average]) / moving_average)
```



