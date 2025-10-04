---
toc: true
title: Highway Convolutions
tags: ['architecture']
date modified: Monday, October 10th 2022, 2:02:26 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# Highway Convolutions
- [Conv](Conv.md)

```python
class HighwayConv1dNew(nn.Conv1d):
    def forward(self, inputs):
        L = super().forward(inputs)
        H1, H2 = rearrange(L, 'b (split c) t -> split b c t', split=2)
        torch.sigmoid_(H1)
        return H1 * H2 + (1.0 - H1) * inputs
```



