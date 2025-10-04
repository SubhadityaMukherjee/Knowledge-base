---
toc: true
title: GELU
tags: ['architecture']
date modified: Monday, October 10th 2022, 2:02:27 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# GELU
- [Paper](https://arxiv.org/abs/1606.08415v4)
- Smoother [Relu](Relu.md)
- $$x\Phi(x)$$ where $\Phi(x)$ is the [Normal Distribution](Normal%20Distribution.md) [CDF](CDF.md)
- Weights inputs by percentile, rather than by sign like [Relu](Relu.md)
- $$GELU(x) = xP(X \leq x) = x\Phi(x) = x. \frac{1}{2}\left[ 1+erf\left( \frac{x}{\sqrt{ 2 }} \right) \right]$$
- If $X \sim \mathscr{N}(0,1)$
- Used in [GPT3](GPT3.md), [Transformer](Transformer.md), [Vision Transformer](Vision%20Transformer.md), [BERT](BERT.md)
- ![](https://production-media.paperswithcode.com/methods/Screen_Shot_2020-05-27_at_12.48.44_PM.png)



