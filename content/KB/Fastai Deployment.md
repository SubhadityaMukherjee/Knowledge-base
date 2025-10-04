---
toc: true
title: Fastai Deployment

tags: ['deeplearning']
date modified: Monday, October 10th 2022, 2:02:28 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# [fastai](fastai.md) Deployment
- [Gradio](Gradio.md)

## Save
```python
from fastai.vision.widgets import *
```

```python
path = Path()
path.ls(file_exts='.pkl')

learn_inf = load_learner(path/'export.pkl')
learn_inf.predict('images/grizzly.jpg')
learn_inf.dls.vocab
```



