---
toc: true
title: Huber/Smooth L1/Smooth MAE
tags: ['loss']
date modified: Monday, October 10th 2022, 2:02:25 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# Huber/Smooth L1/Smooth MAE
- It is less sensitive to outliers than the [MSE](MSE.md) and in some cases prevents exploding #architecture
- [Fast-RCNN](Fast-RCNN)

if $$\left( \left\|y - ŷ\right\| \lt 1.0 \right) >1 $$

$$\frac{1}{\mathrm{length}\left( y \right)} \cdot \mathrm{sum}\left( 0.5 \cdot \left( y - ŷ \right)^{2} \right)$$

else

$$\frac{1}{\mathrm{length}\left( y \right)} \cdot \mathrm{sum}\left( \left\|y - ŷ\right\| - 0.5 \right)$$

## …



