---
toc: true
title: TREEQN
tags: ['einsum']
date modified: Monday, October 10th 2022, 2:02:15 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# TREEQN
```python
def transition(zl):
  # -- [batch_size x num_actions x hidden_dimension]
  return zl.unsqueeze(1) + F.tanh(torch.einsum("bk,aki->bai", [zl, W]) + b)
```



