---
title: Example GCN Layer
toc: true
tags:
  - graph
date modified: Wednesday 30th October 2024, Wed
date created: Wednesday 30th October 2024, Wed
---

# Example GCN Layer
```toc
```

## Example GCN Layer
- ![[Pasted image 20241030114845.webp]]
- ![[Pasted image 20241023120915.webp]]
- this is equivariant, can cope with any number of neighbors, uses the graph srtucture to provide a [[Relational Inductive Bias]] and parameter sharing 

### Example : Graph Classification
- Network to classify molecules as harmless or toxic
- [[Adjacency matrix]] - $$A \in \mathbb{R}^{N \times N}$$
- Node embedding matrix - $$X \in \mathbb{R}^{118 \times N}$$
	- 118 elements of the periodic table
	- vectors of length 118 where every position is zero except for the position corresponding to the relevant element, which is set to one
- ![[Pasted image 20241030114905.webp]]
### Example : Node Classification
- ![[Pasted image 20241030111806.webp]]

