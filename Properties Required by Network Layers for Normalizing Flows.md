---
title: Properties Required by Network Layers for Normalizing Flows
toc: true
tags:
  - architecture
date modified: Tuesday 19th November 2024, Tue
date created: Tuesday 19th November 2024, Tue
---

# Properties Required by Network Layers for Normalizing Flows
```toc
```
- the set of network layers must be suﬀiciently expressive to map a multivariate standard normal distribution to an arbitrary density
- networks should be invertible
- It must be possible to compute the inverse of each layer eﬀiciently
-  It also must be possible to evaluate the determinant of the Jacobian eﬀiciently for either the forward or inverse mapping.