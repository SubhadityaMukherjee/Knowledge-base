---
title: Batching for GNN
toc: true
tags:
  - graph
date modified: Wednesday 30th October 2024, Wed
date created: Wednesday 30th October 2024, Wed
---

# Batching for GNN
```toc
```

## Batching for GNN
- GIven I training graphs ${X_{i}, A_{i}}$ and labels $y_{i}$, params ${\Phi = \{\beta_{k}, \Omega_{k}}\}^{K}_{k=0}$ , [[SGD]]and [[Binary Cross Entropy]]
- We cannot concat batches into a big tensor since each graph has a different number of nodes
- Instead, we treat the graphs in each batch as disjoint components of a single large graph.
- we can then just run the network over this big graph as a single instance of the network equations.
- Then we can do mean pooling on it

### Neighborhood Sampling
- randomly sample fixed number of neighbors, recursively
- somewhat like [[Dropout]]
### Graph Partitioning
- cluster the original graph into disjoint (not connected to each other) subsets of nodes 
- these are batches
- this converts a transductive problem to an inductive one
- for inference, k-hop neighbors

