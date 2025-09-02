---
title: Depth Efficiency of Neural Networks
toc: true
tags:
  - deeplearning
date modified: Tuesday 27th August 2024, Tue
date created: Tuesday 27th August 2024, Tue
---

# Depth Efficiency of Neural Networks
```toc
```
- there are functions that can be realized by deep networks but not by any shallow network whose capacity is bounded above exponentially.
- it would take an exponentially larger number of units in a shallow network to describe these functions accurately
- Eldan & Shamir (2016) showed that when there are multivariate inputs, there is a three-layer network that cannot be realized by any two-layer network if the capacity is sub-exponential in the input dimension.
- Liang & Srikant (2016) show that for a broad class of functions, including univariate functions, shallow networks require exponentially more hidden units than deep networks for a given upper bound on the approximation error