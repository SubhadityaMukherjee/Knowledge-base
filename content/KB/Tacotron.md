---
toc: true
title: Tacotron
tags: ['architecture']
date modified: Monday, October 10th 2022, 2:02:15 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# Tacotron
- CBHG
	- [Conv](Gated Recurrent Unit (GRU|Gated Recurrent Unit (GRU|[GRU](GRU.md)](Conv](Gated Recurrent Unit (GRU|Gated Recurrent Unit (GRU|[GRU](GRU.md).md).md)

```python
class CBHG_Old(nn.Module):
    """CBHG module: a [recurrent](Recurrent.md) neural network composed of:
        - 1-d convolution banks
        - Highway networks + residual connections
        - Bidirectional gated [recurrent](Recurrent.md) units
    """

    def __init__(self, in_dim, K=16, projections=[128, 128]):
        super(CBHG, self).__init__()
        self.in_dim = in_dim
        self.relu = nn.ReLU()
        self.conv1d_banks = nn.ModuleList(
            [BatchNormConv1d(in_dim, in_dim, kernel_size=k, stride=1,
                             padding=k // 2, activation=self.relu)
             for k in range(1, K + 1)])
        self.max_pool1d = nn.MaxPool1d(kernel_size=2, stride=1, padding=1)

        in_sizes = [K * in_dim] + projections[:-1]
        activations = [self.relu] * (len(projections) - 1) + [None]
        self.conv1d_projections = nn.ModuleList(
            [BatchNormConv1d(in_size, out_size, kernel_size=3, stride=1,
                             padding=1, activation=ac)
             for (in_size, out_size, ac) in zip(
                 in_sizes, projections, activations)])

        self.pre_highway = nn.Linear(projections[-1], in_dim, bias=False)
        self.highways = nn.ModuleList(
            [Highway(in_dim, in_dim) for _ in range(4)])

        self.gru = nn.GRU(
            in_dim, in_dim, 1, batch_first=True, bidirectional=True)

def forward_new(self, inputs, input_lengths=None):
    x = rearrange(inputs, 'b t c -> b c t')
    _, _, T = x.shape
    # Concat conv1d bank outputs
    x = rearrange([conv1d(x)[:, :, :T] for conv1d in self.conv1d_banks], 
                 'bank b c t -> b (bank c) t', c=self.in_dim)
    x = self.max_pool1d(x)[:, :, :T]

    for conv1d in self.conv1d_projections:
        x = conv1d(x)
    x = rearrange(x, 'b c t -> b t c')
    if x.size(-1) != self.in_dim:
        x = self.pre_highway(x)

    # Residual connection
    x += inputs
    for highway in self.highways:
        x = highway(x)

    # (B, T_in, in_dim*2)
    outputs, _ = self.gru(self.highways(x))

    return outputs
```



