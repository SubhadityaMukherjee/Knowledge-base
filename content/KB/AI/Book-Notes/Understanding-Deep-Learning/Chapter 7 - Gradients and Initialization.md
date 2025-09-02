---
title: Chapter 7 - Gradients and Initialization
toc: true
tags:
  - gradients
date modified: Wednesday 4th September 2024, Wed
date created: Wednesday 4th September 2024, Wed
---

# Chapter 7 - Gradients and Initialization
```toc
```
- [[Backprop]]
- [[Relu]]
- algorithmic differentiation (I think this means AD?)
- [[Computational Graph]]
- [[Initialization]]
- [[Exploding Gradient]], [[Vanishing Gradient]]
- [[Gradient Checkpointing]]

## Useful Links
- [visualizing weights](https://distill.pub/2020/circuits/visualizing-weights/)
- [all you need is a good init](https://arxiv.org/abs/1511.06422)
- [how to initialize a neural network](https://pouannes.github.io/blog/initialization/)
- [Difficulty of training networks by xavier and yoshua bengio](https://proceedings.mlr.press/v9/glorot10a)
- netron, tensorboard and pytorchviz for visualizing computational graphs

## Qs
- If a network can learn things anyway, why does initaliziation make such a big difference?
- How can we make backprop more efficient? (aka how does it work in PyTorch/TF)