---
toc: true
title: Weight Decay Vs L2 Regularization
tags: ['regularization']
---

## Weight Decay Vs L2 Regularization
- L2 regularization is a classic method to reduce over-fitting, and consists in adding to the loss function the sum of the squares of all the weights of the model, multiplied by a given hyper-parameter
```python
final_loss = loss + wd * all_weights.pow(2).sum() / 2
```
- where wd is the hyper-parameter to set
- This is also called weight decay, because when applying vanilla SGD it's equivalent to updating the weight like this
```python
w = w - lr * w.grad - lr * wd * w
```
- In this equation we see how we subtract a little portion of the weight at each step, hence the name decay
- So why make a distinction between those two concepts if they are the same thing
- The answer is that they are only the same thing for vanilla SGD, but as soon as we add momentum, or use a more sophisticated optimizer like Adam, L2 regularization (first equation) and weight decay (second equation) become different
- When using the Adam optimizer, it gets even more different: in the case of L2 regularization we add this $wd\times w$ to the gradients then compute a moving average of the gradients and their squares before using both of them for the update. Whereas the weight decay method simply consists in doing the update, then subtract to each weight.
- And after experimenting with this, Ilya Loshchilov and Frank Hutter suggest in their article we should use weight decay with Adam, and not the L2 regularization that classic deep learning libraries implement.
- Inside the step function of the optimizer, only the gradients are used to modify the parameters, the value of the parameters themselves isn't used at all
- It still has to be done after the gradients are computed
- the optimizer should have been set with wd=0 otherwise it will do some L2 regularization, which is exactly what we don't want
- loop over all the parameters and do our little weight decay update



