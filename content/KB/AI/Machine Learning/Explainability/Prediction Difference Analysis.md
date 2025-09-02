---
toc: true
title: Prediction Difference Analysis

tags: ['explainability']
date modified: Wednesday, October 12th 2022, 4:44:23 pm
date created: Wednesday, October 12th 2022, 4:44:22 pm
---

# Prediction Difference Analysis


- Their goal was to improve and interpret DNNs. Their technique was based on the univariate approach of [94] and the idea that the relevance of an input feature with respect to a class can be estimated by measuring how the prediction changes if the feature is removed. Zintgraf et al. removed several features at one time using their knowledge about the images by strategically choosing patches of connected pixels as the feature sets. Instead of going through all individual pixels, they considered all patches of a special size implemented in a sliding window fashion. They visualized the effects of different window sizes and marginal versus conditional sampling and displayed feature maps of different hidden layers and top-scoring classes.



