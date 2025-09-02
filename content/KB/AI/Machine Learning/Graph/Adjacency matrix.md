---
title: Adjacency matrix
toc: true
tags:
  - graph
date modified: Tuesday 22nd October 2024, Tue
date created: Tuesday 22nd October 2024, Tue
---

# Adjacency Matrix
```toc
```
- NxN matrix where (m,n) is set if there is an edge between the nodes m and n or 0 otherwise
- For undirected graphs, this is always symmetric
- For large sparse ones, it can be a list of connections to save memory
- The $n^{th}$ node has an associated node embedding x(n) of length D. These embeddings are concatenated and stored in the D×N node data matrix X. Similarly, the $e^{th}$ edge has an associated edge embedding e(e) of length DE . These edge embeddings are collected into the $D_E ×E$ matrix E.

## [[Properties of Adjacency matrix]]