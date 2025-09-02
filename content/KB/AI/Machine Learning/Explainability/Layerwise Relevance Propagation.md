---
toc: true
title: Layerwise Relevance Propagation

tags: ['explainability']
date modified: Wednesday, October 12th 2022, 4:43:47 pm
date created: Wednesday, October 12th 2022, 4:43:45 pm
---

# Layerwise Relevance Propagation


- It relies on a conservation principle to propagate the outcome decision back without using gradients. The idea behind it is a decomposition of prediction function as a sum of layerwise relevance values. When LRP is applied to deep ReLU networks, LRP can be understood as a deep Taylor decomposition of the prediction. This principle ensures that the prediction activity is fully redistributed through all the layers onto the input variables
- suffers from the shattered gradients problem



