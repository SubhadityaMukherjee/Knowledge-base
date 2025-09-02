---
toc: true
title: Pytorch Tricks

tags: ['deeplearning']
date modified: Monday, October 10th 2022, 2:02:19 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# Pytorch Tricks
- Also look at [fastai](fastai.md)

## Get Params of a Layer
```python
m = learn.model
l = m.get_submodule('0.model.stem.1')
list(l.parameters())
```

## Interact
```python
from ipywidgets import interact
@interact(m=1.5, b=1.5)
def plot_relu(m,b):
	plot_function(partial(relu, m, b), ylim = (-1, 4))
```

## Set Dataset Directory
```python
import os
os.environ["TORCH_HOME"] = "/media/hdd/Datasets/"
os.environ["FASTAI_HOME"] = "/media/hdd/Datasets/"
```



