---
toc: true
title: Amsgrad

tags: ['optimizer']
date modified: Thursday 11th May 2023, Thu
date created: Thursday 11th May 2023, Thu
---

# Amsgrad


## Modified [[Adam]]
- By analyzing the proof of convergence for the Adam optimizer, they spotted a mistake in the update rule that could cause the algorithm to converge to a sub-optimal point
- update rule of Adam
```python
avg_grads = beta1 * avg_grads + (1-beta1) * w.grad 
avg_squared = beta2 * (avg_squared) + (1-beta2) * (w.grad ** 2) 
w = w - lr * avg_grads / sqrt(avg_squared)
```
- We've just skipped the bias correction (useful for the beginning of training) to focus on the important point
- The error in the proof of Adam the authors spotted is that it requires the quantity
```python
lr / sqrt(avg_squared)
```
- which is the step we take in the direction of our average gradients, to be decreasing over training
- Since the learning rate is often taken constant or decreasing (except for crazy people like us trying to obtain super-convergence), the fix the authors proposed was to force the avg_squared quantity to be increasing by adding another variable to keep track of their maximums.
- Implementing amsgrad
- This causes the weight update code from the previous section to be changed to something like this:

## Results
- Amsgrad turns out to be very disappointing. In none of our experiments did we find that it helped the slightest bit, and even if it's true that the minimum found by amsgrad is sometimes slightly lower (in terms of loss) than the one reached by Adam, the metrics (accuracy, f1 score...) always end up worse
- The proof of convergence for the Adam optimizer in deep learning (since it's for convex problems) and the mistake they found in it mattered for synthetic experiments that have nothing to do with real-
- life problems. Actual tests show that when those avg_squared gradients want to decrease, it's best for the final result to do so.



