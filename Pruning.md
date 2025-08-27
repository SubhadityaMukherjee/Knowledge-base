---
toc: true
title: Pruning
tags:
  - regularization
date modified: Monday, October 10th 2022, 2:02:19 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# Pruning
- Mainly that of being able to reduce the size, cost and computational requirements of my models, all while maintaning the accuracy (sort of atleast).
- Generally this comes about by removing parameters in some form or fashion.
- Rather than taking a mask, we can prune certain parts of the network by setting them to 0 or by dropping them if required. (aka weights and biases)
- In most cases, the network is first trained for a while. Then pruned. Which reduces its accuracy and is thus trained again (fine tuning). This cycle is repeated until we get the results we require.
- Major Types of Pruning Methods
- [Structure Based Pruning](./Structure%2520Based%2520Pruning.md#)
- [Scoring Pruning Approaches](./Scoring%2520Pruning%2520Approaches.md#)
- [Scheduling](./Scheduling.md#)
- [Fine Tuning Based Pruning](./Fine%2520Tuning%2520Based%2520Pruning.md#)
- [Global Magnitude Based Pruning](./Global%2520Magnitude%2520Based%2520Pruning.md#)
- [Global Gradient Magnitude Based Pruning](./Global%2520Gradient%2520Magnitude%2520Based%2520Pruning.md#)
- [Layerwise Gradient Magnitude Based Pruning](./Layerwise%2520Gradient%2520Magnitude%2520Based%2520Pruning.md#)
- [Random Pruning](./Random%2520Pruning.md#)
- [Layerwise Magnitude Based Pruning](./Layerwise%2520Magnitude%2520Based%2520Pruning.md#)



