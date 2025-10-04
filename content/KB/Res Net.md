---
toc: true
title: Res Net
tags: ['architecture']
date modified: Monday, November 28th 2022, 11:50:26 am
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# Res Net
- @heDeepResidualLearning2016
- [Deep Residual Learning for Image Recognition](https://arxiv.org/abs/1512.03385)
- Deeper Networks have [Issues](Issues.md) because of vanishing #architecture
- Propagate gradients forward for deeper networks
- Skip connections
- output of F(x) has the same dims as x -> add
- If only spatial dims match (aka not channels) -> concat
- less params than [Vgg](Vgg.md)
- [Skip Connection](Skip%20Connection.md)
- Sadly, one of the creators Jian Sun passed away yesterday. (16-6-22)

```python
def make_layer(inplanes, planes, block, n_blocks, stride=1):
    downsample = None
    if stride != 1 or inplanes != planes * block.expansion:
        # output size won't match input, so adjust residual
        downsample = nn.Sequential(
            nn.Conv2d(inplanes, planes * block.expansion,
                      kernel_size=1, stride=stride, bias=False),
            nn.BatchNorm2d(planes * block.expansion),
        )
    return nn.Sequential(
        block(inplanes, planes, stride, downsample),
        *[block(planes * block.expansion, planes) for _ in range(1, n_blocks)]
    )

def ResNetNew(block, layers, num_classes=1000):    
    e = block.expansion
    
    resnet = nn.Sequential(
        Rearrange('b c h w -> b c h w', c=3, h=224, w=224),
        nn.Conv2d(3, 64, kernel_size=7, stride=2, padding=3, bias=False),
        nn.BatchNorm2d(64),
        nn.ReLU(inplace=True),
        nn.MaxPool2d(kernel_size=3, stride=2, padding=1),
        make_layer(64,      64,  block, layers[0], stride=1),
        make_layer(64 * e,  128, block, layers[1], stride=2),
        make_layer(128 * e, 256, block, layers[2], stride=2),
        make_layer(256 * e, 512, block, layers[3], stride=2),
        # combined AvgPool and view in one averaging operation
        Reduce('b c h w -> b c', 'mean'),
        nn.Linear(512 * e, num_classes),
    )
    
    # [initialization](Initialization.md)
    for m in resnet.modules():
        if isinstance(m, nn.Conv2d):
            n = m.kernel_size[0] * m.kernel_size[1] * m.out_channels
            m.weight.data.normal_(0, math.sqrt(2. / n))
        elif isinstance(m, nn.BatchNorm2d):
            m.weight.data.fill_(1)
            m.bias.data.zero_()
    return resnet
```



