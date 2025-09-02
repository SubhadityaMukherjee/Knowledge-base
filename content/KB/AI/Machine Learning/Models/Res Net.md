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
- Deeper Networks have [Issues](Issues.md) because of [[Vanishing Gradient]]
- Propagate gradients forward for deeper networks
- output of F(x) has the same dims as x -> add
- If only spatial dims match (aka not channels) -> concat
- less params than [Vgg](Vgg.md)
- [[Skip Connection]]
- Sadly, one of the creators Jian Sun passed away yesterday. (16-6-22)