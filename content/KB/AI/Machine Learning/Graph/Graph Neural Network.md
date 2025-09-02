---
title: Graph Neural Network
toc: true
tags:
  - graph
  - architecture
date modified: Tuesday 22nd October 2024, Tue
date created: Tuesday 22nd October 2024, Tue
---

# Graph Neural Network
```toc
```
- model that takes the node embeddings X and the adjacency matrix A as inputs and passes them through a series of K layers. 
- The node embeddings are updated at each layer to create intermediate "hidden" representations $H_{k}$ before finally computing output embeddings $H_{K}$
- At the start of this network, each column of the input node embeddings X just contains information about the node itself. At the end, each column of the model output $H_K$ includes information about the node and its context within the graph.
- similar to word [[Embedding]] for [[Transformer]]
- ![[Pasted image 20241022125245.webp]]

## [[Graph Level Tasks]]

## [[Node Level Tasks]]
## [[Edge Prediction Tasks]]
