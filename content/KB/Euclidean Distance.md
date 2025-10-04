---
toc: true
title: Euclidean Distance

tags: ['loss']
date modified: Monday, October 10th 2022, 2:02:28 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# Euclidean Distance
- $$d = \sqrt{\Sigma_{i=1}^{n}(p_{i}-q_{i})^{2}}$$
- It is a distance measure that best can be explained as the length of a segment connecting two points.
- calculated from the cartesian coordinates of the points using the Pythagorean theorem
- Euclidean distance is not scale in-variant which means that distances computed might be skewed depending on the units of the [Features](Features.md). Typically, one needs to normalize the data before using this distance measure.
- Moreover, as the dimensionality increases of your data, the less useful Euclidean distance becomes. This has to do with the [Curse Of Dimensionality](Curse%20Of%20Dimensionality.md)
- works great when you have low-dimensional data and the magnitude of the vectors is important to be measured



