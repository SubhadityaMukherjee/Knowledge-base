---
toc: true
title: One cycle policy

tags: ['optimizer']
date modified: Thursday 11th May 2023, Thu
date created: Thursday 11th May 2023, Thu
---

# One Cycle Policy


- @smithSuperConvergenceVeryFast2018

## Step
- recommends to do a cycle with two steps of equal lengths, one going from a lower learning rate to a higher one than go back to the minimumThe maximum should be the value picked with the Learning Rate Finder, and the lower one can be ten times lower
- Then, the length of this cycle should be slightly less than the total number of epochs, and, in the last part of training, we should allow the learning rate to decrease more than the minimum, by several orders of magnitude.
- The idea of starting slower isn't new: using a lower value to warm-up the training is ofen done, and this is exactly what the first part is achieving
- Leslie doesn't recommend to switch to a higher value directly, however, but to rather slowly go there linearly, and to take as much time going up as going down.
- the during the middle of the cycle, the high learning rates will act as regularization method, and keep the network from overfitting
- They will prevent the model to land in a steep area of the loss function, preferring to find a minimum that is flatteapproximates of the hessian were lower, indicating that the SGD was finding a wider flat area
- Then the last part of the training, with descending learning rates up until annihilation will allow us to go inside a steeper local minimum inside that smoother part
- Surprisingly, applying this policy even allows us to pick larger maximum learning rates, closer to the minimum of the plot we draw when using the learning rate finder
- Those trainings are a bit more dangerous in the sense that the loss can go too far away and make the whole thing diverge In those cases, it can be worth to try with a longer cycle before going to a slower learning rate, since a long warm-up seems to help
- ![](../images/Pasted%20image%2020230511123527.png)

## Cyclical Momentum
- To accompany the movement toward larger learning rates, Leslie found in his experiments that decreasing the momentum led to better results
- This supports the intuition that in that part of the training, we want the SGD to quickly go in new directions to find a flatter area, so the new gradients need to be given more weight
- According to Leslie, the exact best value of momentum chosen during the whole training can give us the same final results, but using cyclical momentums removes the hassle of trying multiple values and running several full cycles, losing precious time.
- In his opinion, the batch size should be set to the highest possible value to fit in the available memory. Then the other hyper-parameters we may have (dropout for instance) can be tuned the same way as weight decay, or just by trying on a cycle and see the results they give
- Training with the 1cycle policy at high learning rates is a method of regularization in itself, so we shouldn't be surprised if we have to reduce the other forms of regularization we were previously using when we put it in place
- ![](../images/Pasted%20image%2020230511123512.png)



