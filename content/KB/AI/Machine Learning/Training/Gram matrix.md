---
toc: true
title: Gram matrix
tags: ['einsum']
date modified: Monday, October 10th 2022, 2:02:26 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# Gram Matrix
```python
def gram_matrix_new(y):
    b, ch, h, w = y.shape
    return torch.einsum('bchw,bdhw->bcd', [y, y]) / (h * w)
```



