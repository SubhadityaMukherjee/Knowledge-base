---
toc: true
title: Layerwise Magnitude Based Pruning
tags: ['regularization']
date modified: Monday, October 10th 2022, 2:02:24 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# Layerwise Magnitude Based [Pruning](Pruning.md)
- Takes the lowest values per layer in the network and prunes.
- Modifying the global layerwise and applying it per layer instead.
- To do this, we first make a copy of the weights. Then for every layer in the array, we find the least n values, take the nth value and set all the others to 0.
- As an edge case, if the number of elements entered is greater than the total length of the layer, then the entire layer is set to 0.



