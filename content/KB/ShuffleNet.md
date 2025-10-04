---
toc: true
title: ShuffleNet
tags: ['architecture']
date modified: Monday, October 10th 2022, 2:02:17 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# ShuffleNet
- Channel Shuffle

```python
def channel_shuffle_new(x, groups):
    return rearrange(x, 'b (c1 c2) h w -> b (c2 c1) h w', c1=groups)
```

```python
class ShuffleUnitNew(nn.Module):
    def __init__(self, in_channels, out_channels, groups=3, 
                 grouped_conv=True, combine='add'):
        super().__init__()
        first_1x1_groups = groups if grouped_conv else 1
        bottleneck_channels = out_channels // 4
        self.combine = combine
        if combine == 'add':
            # ShuffleUnit Figure 2b
            self.left = Rearrange('...->...') # identity
            depthwise_stride = 1
        else:
            # ShuffleUnit Figure 2c
            self.left = nn.AvgPool2d(kernel_size=3, stride=2, padding=1)
            depthwise_stride = 2
            # ensure output of concat has the same channels as original output channels.
            out_channels -= in_channels
            assert out_channels > 0

        self.right = nn.Sequential(
            # Use a 1x1 grouped or non-grouped convolution to reduce input channels
            # to bottleneck channels, as in a ResNet bottleneck module.
            conv1x1(in_channels, bottleneck_channels, groups=first_1x1_groups),
            nn.BatchNorm2d(bottleneck_channels),
            nn.ReLU(inplace=True),
            # channel shuffle
            Rearrange('b (c1 c2) h w -> b (c2 c1) h w', c1=groups),
            # 3x3 depthwise convolution followed by batch 
            conv3x3(bottleneck_channels, bottleneck_channels,
                    stride=depthwise_stride, groups=bottleneck_channels),
            nn.BatchNorm2d(bottleneck_channels),
            # Use 1x1 grouped convolution to expand from 
            # bottleneck_channels to out_channels
            conv1x1(bottleneck_channels, out_channels, groups=groups),
            nn.BatchNorm2d(out_channels),
        )        
        
    def forward(self, x):
        if self.combine == 'add':
            combined = self.left(x) + self.right(x)
        else:
            combined = torch.cat([self.left(x), self.right(x)], dim=1)
        return F.relu(combined, inplace=True)
```



