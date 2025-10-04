---
toc: true
title: Iterative Closest Point
tags: ['robotics']
---

# Iterative Closest Point
- Start from initial guess
- Iterate
- For each point on M, find closest point on P
- Find best transform for this correspondence Transform M
- Good initial guess -> Converges to global minimum
- The ICP is applicable when we have a relatively good starting point in advance.
- Otherwise, it will be trapped into the first local minimum and the solution will be useless.
- Without pose information, ICP-based approaches are unable to recover the proper transformations because of the ambiguity in surface matching.
- ![](../images/Pasted%20image%2020221103123325.png)



