---
title: Non Maxima Supression
toc: true
tags:
  - architecture
date modified: Wednesday 2nd October 2024, Wed
date created: Wednesday 2nd October 2024, Wed
---

# Non Maxima Supression
```toc
```
- ![[Pasted image 20241002114638.webp]]
- $$Intersection Over Union(IoU) = (Target ∩ Prediction) / (Target U Prediction)$$
- In our case using BBoxes, it can be modified to,

$$IOU(Box1, Box2) = Intersection_Size(Box1, Box2) / Union_Size(Box1, Box2)$$