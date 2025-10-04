---
toc: true
title: Log Cosh
tags: ['loss']
date modified: Monday, October 10th 2022, 2:02:23 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# Log Cosh
- works like the [MSE](MSE.md), but is smoothed towards large errors (presumably caused by outliers) so that the final error score isn’t impacted thoroughly.

We first define the [Softplus](Softplus.md) function $$\log\left( e^{x} + 1 \right)$$

Then , $$x = ŷ - y$$

logcosh = $$\mathrm{mean}\left( x + \mathrm{softplus}\left( -2 \cdot x \right) - \log\left( 2.0 \right) \right)$$

## …



