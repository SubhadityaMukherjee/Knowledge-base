---
title: ELBO loss
toc: true
tags:
  - loss
date modified: Tuesday 19th November 2024, Tue
date created: Tuesday 19th November 2024, Tue
---

# ELBO Loss
```toc
```
- $$\log p_\theta(x_{i}) \geq \mathbb{E}_{z\sim q_{\theta (z | x_{i})}}log(p_\theta(x_{i}|z))- KL{q_\theta(z|x_{i})||p(z)}$$
- KL is[[KL Divergence]]