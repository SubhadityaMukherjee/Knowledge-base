---
toc: true
title: Manhattan Distance

tags: ['loss']
date modified: Monday, October 10th 2022, 2:02:22 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# Manhattan Distance
- Taxicab distance or City Block distance, calculates the distance between real-valued vectors
- $$D(x,y) = \Sigma_{i=1}^{k}|x_{i}-y_{i}|$$
- There is no diagonal movement involved in calculating the distance.
- Manhattan distance seems to work okay for high dim data, it is a measure that is somewhat less intuitive than [Euclidean Distance](Euclidean%20Distance.md), especially when using in high-dimensional data
- more likely to give a higher distance value than [Euclidean Distance](Euclidean%20Distance.md) since it does not the shortest path possible.
- When your dataset has discrete and/or binary attributes, Manhattan seems to work quite well since it takes into account the paths that realistically could be taken within values of those attributes.



