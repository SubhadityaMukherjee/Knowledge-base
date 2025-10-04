---
toc: true
title: DeepNorm

tags: ['regularization']
date modified: Monday, October 10th 2022, 2:02:30 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# DeepNorm
- which modifies the residual connection in Transformers
- theoretical justification of bounding the model update by a constant which makes stable training possible in a principled way
- DeepNorm modifies the residual connection in the Transformer architecture by up-scaling it before performing [Layer Normalization](Layer%20Normalization.md)



