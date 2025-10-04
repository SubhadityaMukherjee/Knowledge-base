---
toc: true
title: Saliency vs Attention
tags: ['explainability']
---


## Saliency Vs Attention
- Input saliency methods are addressing the goal head-on: they reveal why one particular model prediction was made in terms of how relevant each input word was to that prediction
- input saliency methods typically take the entire computation path into account, all the way from the input word embeddings to the target output prediction value
- Attention weights do not: they reflect, at one point in the computation, how much the model attends to each input representation, but those representations might already have mixed in information from other inputs
- Ironically, attention-as-explanation is sometimes evaluated by comparing it against gradient-based measures, which again begs the question why we wouldn't use those measures in the first place
- In terms of efficiency, it is true that for attention only a forward pass is required, but many other methods discussed at most require a forward and then a backward pass, which is still extremely efficient.



