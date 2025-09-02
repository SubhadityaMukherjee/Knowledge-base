---
toc: true
title: Xavier Initialization
tags: ['regularization']
date modified: Monday, October 10th 2022, 2:02:13 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# Xavier [Initialization](Initialization.md)
- $$\mathrm{a=\sqrt{\frac{6}{\left(\mathrm{d}\mathrm{_{\mathrm{in}}^{\mathrm{ }}}+\mathrm{d}_{\mathrm{out}} \right)}}}$$
- Random values drawn uniformly from $[-a,a]$
- For [Batch Normalization](Batch%20Normalization.md) [Layers](Layers.md), $\gamma =1$ and $\beta=0$
- For [Tanh](Tanh.md) based activating neural nets



