---
toc: true
title: Spatial Transformer
tags: ['architecture']
date modified: Monday, October 10th 2022, 2:02:16 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# Spatial [Transformer](Transformer.md)
- [Transformer](Transformer.md)

```python
class SpacialTransformNew(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        # Spatial [Transformer|[transformer](Transformer.md) localization-network
        linear = nn.Linear(32, 3 * 2)
        # Initialize the weights/bias with identity transformation
        linear.weight.data.zero_()
        linear.bias.data.copy_(torch.tensor([1, 0, 0, 0, 1, 0], dtype=torch.float))
        
        self.compute_theta = nn.Sequential(
            nn.Conv2d(1, 8, kernel_size=7),
            nn.MaxPool2d(2, stride=2),
            nn.ReLU(True),
            nn.Conv2d(8, 10, kernel_size=5),
            nn.MaxPool2d(2, stride=2),
            nn.ReLU(True),
            Rearrange('b c h w -> b (c h w)', h=3, w=3),
            nn.Linear(10 * 3 * 3, 32),
            nn.ReLU(True),
            linear,
            Rearrange('b (row col) -> b row col', row=2, col=3),
        )

    # Spatial transformer network forward function
    def stn(self, x):
        grid = F.affine_grid(self.compute_theta(x), x.size())
        return F.grid_sample(x, grid)
```



