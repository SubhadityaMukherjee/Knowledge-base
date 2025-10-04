---
toc: true
title: Identity Loss

tags: ['loss']
date modified: Sunday, December 11th 2022, 1:33:20 pm
date created: Sunday, December 11th 2022, 1:26:44 pm
---

# Identity Loss

- $$L_{identity}(G,F) = \mathbb{E}_{y \sim p_{data}(y)}[||G(y)-y)||_{1}] + \mathbb{E}_{x \sim p_{data}(x)}[||F(x)-x)||_{1}]$$
- The identity loss is used to preserve the color and prevent reverse color in the result.
- This loss can regularize the generator to be near an identity mapping when real samples of the target domain are provided. If something already looks like from the target domain, you should not map it into a different image.
- The model will be more conservative for unknown content.
- In general, it can help bette preserve the content if that is your priority.



