---
title: Properties of Adjacency matrix
toc: true
tags:
  - graph
date modified: Tuesday 22nd October 2024, Tue
date created: Tuesday 22nd October 2024, Tue
---

# Properties of Adjacency Matrix
```toc
```

## Properties of [[Adjacency matrix]]
- if we raise the adjacency matrix to the power of L, the entry at position (m,n) of $A^L$ contains the number of unique walks of length L from node n to node m
	- ![[Pasted image 20241030114233.webp]]
- Node indexing is arbitrary
- Permutation matrix
	- matrix where exactly one entry in each row and column take the value one, and the remaining values are zero
	- When position (m,n) of the permutation matrix is set to one, it indicates that node mwill become node nafter the permutation.
	- $$X' = XP ; A' = P^{T}AP$$
	- post-multiplying by P permutes the columns and pre-multiplying by $P^T$ permutes the rows