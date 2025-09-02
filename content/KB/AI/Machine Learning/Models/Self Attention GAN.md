---
toc: true
title: Self Attention GAN
tags: ['architecture']
date modified: Monday, October 10th 2022, 2:02:17 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# [Self Attention](Self%20Attention.md) GAN
- [Self Attention](Self%20Attention.md) + [Generative Models](Generative%20Models.md)

```python
class Self_Attn_New(nn.Module):
    """ Self attention Layer"""
    def __init__(self, in_dim):
        super().__init__()
        self.query_conv = nn.Conv2d(in_dim, out_channels=in_dim//8, kernel_size=1)
        self.key_conv = nn.Conv2d(in_dim, out_channels=in_dim//8, kernel_size=1)
        self.value_conv = nn.Conv2d(in_dim, out_channels=in_dim, kernel_size=1)
        self.gamma = nn.Parameter(torch.zeros([1]))

    def forward(self, x):
        proj_query = rearrange(self.query_conv(x), 'b c h w -> b (h w) c')
        proj_key = rearrange(self.key_conv(x), 'b c h w -> b c (h w)')
        proj_value = rearrange(self.value_conv(x), 'b c h w -> b (h w) c')
        energy = torch.bmm(proj_query, proj_key)
        attention = F.softmax(energy, dim=2)
        out = torch.bmm(attention, proj_value)
        out = x + self.gamma * rearrange(out, 'b (h w) c -> b c h w',
                                         **parse_shape(x, 'b c h w'))
        return out, attention
```



