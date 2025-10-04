---
toc: true
title: Multi Head Attention
tags: ['architecture']
date modified: Monday, October 10th 2022, 2:02:21 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# Multi Head [Attention](Attention.md)
- [ZihangDai et al., 2019](https://arxiv.org/abs/1901.02860)
- which computes self-[Attention](Attention.md) over the inputs, then adds back the residual and layer normalizes everything. The [Attention](Attention.md) head can be split into multiple segments, hence the name _multi-head_
- Multiple [Attention](Attention.md) instances, each focusing on a different part of the input
- Words can mean different things in context
	- If using [Self Attention](Self%20Attention.md), then this just gets summed up. Which is not very nice
	- Several [Attention](Attention.md) heads -> different output vectors
	- Concatenate them and pass through a linear transform -> dimension back to k
- $$MultiHead(Q,K,V) = Concat(head_1, head_2, …., head_h)W^O$$
	- $$head_i = Attention(QW_i^Q, KW_i^K , VW_i^V)$$
- W is learnable projections for [Attention](Attention.md) params
- ![](../images/Pasted%20image%2020220307183058.png)
- To improve efficiency
	- Cut the incoming vector into chunks -> no of [Attention](Attention.md) heads

```python
class MultiHeadAttentionNew(nn.Module):
    def __init__(self, n_head, d_model, d_k, d_v, dropout=0.1):
        super().__init__()
        self.n_head = n_head
        
        self.w_qs = nn.Linear(d_model, n_head * d_k)
        self.w_ks = nn.Linear(d_model, n_head * d_k)
        self.w_vs = nn.Linear(d_model, n_head * d_v)
        
        nn.init.normal_(self.w_qs.weight, mean=0, std=np.sqrt(2.0 / (d_model + d_k)))
        nn.init.normal_(self.w_ks.weight, mean=0, std=np.sqrt(2.0 / (d_model + d_k)))
        nn.init.normal_(self.w_vs.weight, mean=0, std=np.sqrt(2.0 / (d_model + d_v)))
        
        self.fc = nn.Linear(n_head * d_v, d_model)
        nn.init.xavier_normal_(self.fc.weight)
        self.dropout = nn.Dropout(p=dropout)
        self.layer_norm = nn.LayerNorm(d_model)

    def forward(self, q, k, v, mask=None):
        residual = q
        q = rearrange(self.w_qs(q), 'b l (head k) -> head b l k', head=self.n_head)
        k = rearrange(self.w_ks(k), 'b t (head k) -> head b t k', head=self.n_head)
        v = rearrange(self.w_vs(v), 'b t (head v) -> head b t v', head=self.n_head)
        attn = torch.einsum('hblk,hbtk->hblt', [q, k]) / np.sqrt(q.shape[-1])
        if mask is not None:
            attn = attn.masked_fill(mask[None], -np.inf)
        attn = torch.softmax(attn, dim=3)
        output = torch.einsum('hblt,hbtv->hblv', [attn, v])
        output = rearrange(output, 'head b l v -> b l (head v)')
        output = self.dropout(self.fc(output))
        output = self.layer_norm(output + residual)
        return output, attn
```



