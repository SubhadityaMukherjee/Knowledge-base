---
title: Loss for multiclass classification
toc: true
tags:
  - loss
date modified: Wednesday 28th August 2024, Wed
date created: Wednesday 28th August 2024, Wed
---

# Loss for multiclass classification
```toc
```
- Map $x$ to one of $K > 2$ classes
- Distribution - [Categorical Distribution](Categorical%20Distribution.md)
- The parameters are constrained to take values between zero and one, and they must collectively sum to one to ensure a valid probability distribution $$Pr(y=k) = \lambda_{k}$$
- Network computes $K$ params from input x
- Since the output of the network does not conform to the format, we use [Softmax](Softmax.md) so results are positive, and the K numbers sum to one
- ![](Pasted%20image%2020240828102028.webp)
- Loss function : [Negative Log Likelihood](Negative%20Log%20Likelihood.md)
- This is then - [Cross Entropy](Cross%20Entropy.md)
- ![](Pasted%20image%2020240828102204.webp)