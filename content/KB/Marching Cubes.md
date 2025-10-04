---
toc: true
title: Marching Cubes
tags: ['visualization']
date modified: Monday, October 10th 2022, 2:02:22 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# Marching Cubes
- 3D version of [Marching Squares](Marching%20Squares.md)
- Cell consists of 8 node values: (i+{0,1}, j+{0,1}, k+{0,1})
- 1. Consider a cell
- 2. Classify each vertex as inside or outside
- 3. Build an index
- 4. Get edge list from table[index]
- 5. Interpolate the edge location
- $$x = i + \frac{(c-v[i])}{(v[i+1]-v[i])}$$
- 6. Compute gradients
- [Finite Differences](Finite%20Differences.md) Central
- 7. Consider ambiguous cases
- [Midpoint Decider](Midpoint%20Decider.md)
- [Asymptotic Decider](Asymptotic%20Decider.md)
- 8. Go to next cell
- ![](../images/Pasted%20image%2020220417235937.png)

## Limitations
- Produces many triangles
- Cannot represent sharp edges
- Produces “ugly” (thin) triangles
- Produces ringing artifacts!



