---
toc: true
title: Gradient Clipping

tags: ['architecture']
date modified: Monday, October 10th 2022, 2:02:26 pm
date created: Thursday, July 28th 2022, 5:59:06 pm
---

# Gradient Clipping
- Limit the value or the norm of a gradient to a fixed Hyperparameter λ.
- mitigate the Vanishing & Exploding Gradients, exploding ones
- idea is to [CLIP](CLIP.md) the gradients during Backpropagation to a certain threshold (limit the value)
- most often used in RNN or GAN, where Batch Normalisation is tricky to use
- methods
    - [CLIP](CLIP.md) by norm
        - [CLIP](CLIP.md) the whole gradient if its L2 norm is greater than the threshold
        - remains the orientation
    - [CLIP](CLIP.md) by value
        - [CLIP](CLIP.md) the gradient by a fixed value
        - problem: orientation of the gradient may change due to clipping
            - example: \[0.9,100.0\]→\[0.9,1.0\]
            - however, this works well in practice
- pros:
    - larger batch sizes
- cons:
    - sensible to tuning Hyperparameter λ
- [Adaptive Gradient Clipping](Adaptive%20Gradient%20Clipping.md)



