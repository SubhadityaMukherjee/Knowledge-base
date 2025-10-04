---
toc: true
title: FastText
tags: ['architecture']
date modified: Monday, October 10th 2022, 2:02:28 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# FastText
```python
def FastTextNew(vocab_size, embedding_dim, output_dim):
    return nn.Sequential(
        Rearrange('t b -> t b'),
        nn.Embedding(vocab_size, embedding_dim),
        Reduce('t b c -> b c', 'mean'),
        nn.Linear(embedding_dim, output_dim),
        Rearrange('b c -> b c'),
    )
```



