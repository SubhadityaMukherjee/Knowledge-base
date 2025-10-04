---
toc: true
title: Normalized Inverted Structural Similarity Index

tags: ['explainability']
date modified: Monday, October 10th 2022, 2:02:08 pm
date created: Wednesday, October 5th 2022, 2:55:16 pm
---

# Normalized Inverted [Structural Similarity Index](Structural%20Similarity%20Index.md)
- metric is calculated from [Structural Similarity Index](Structural%20Similarity%20Index.md) by inverting the range and then normalizing it.
- NISSIM bounds to (0, 1] where 0 means similar and 1 means dissimilar. Ideally we want this value as close to 0 as possible
- $$NISSIM_{i}= \frac{1-SSIM_{i}}{2}$$



