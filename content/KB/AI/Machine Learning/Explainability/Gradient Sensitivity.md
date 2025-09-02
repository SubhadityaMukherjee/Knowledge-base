---
toc: true
title: Gradient Sensitivity

tags: ['explainability']
date modified: Friday 24th March 2023, Fri
date created: Friday 24th March 2023, Fri
---

# Gradient Sensitivity


- if for every input and baseline that differ in one feature but have different predictions, then the differing feature should be given a non-zero attribution
- If the function implemented by the deep network does not depend (mathematically) on some variable, then the attribution to that variable is always zero.
- The sensitivity axiom introduces the baseline
- A baseline is defined as an absence of a feature in an input
- This definition is confusing, especially when dealing with complex models, but the baseline could be interpreted as “input from the input space that produces a neutral prediction”.
- A baseline can be treated as an input to produce a counterfactual explanation by checking how the model behaves when moving from baseline to the original image.
- The authors give the example of the baseline for an object recognition network, which is a black image.
- Authors argue that gradient-based methods are violating Sensitivity
- As an example, we are presented with the case of simple function, $$f(x)=1-ReLU(1-x)$$ 
- and the baseline being $x=0$
- When trying to generate attribution for $x=2$, the functions’ output changes from 0 to 1 but after $x=1$, it becomes flat and causes the gradient to equal zero.
- Obviously, x attributes to the result, but because the function is flat at the input we are testing results in invalid attribution and breaks the Sensitivity
- Sundararajan et al. think that breaking Sensitivity causes gradients to focus on irrelevant features.



