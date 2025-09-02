---
toc: true
title: Instance Normalization
tags:
  - architecture
  - normalization
date modified: Sunday, December 11th 2022, 1:16:14 pm
date created: Sunday, December 11th 2022, 1:15:01 pm
---

# Instance Normalization

- Contrast Normalization
- $$
    y_{tijk} = \frac{x_{tijk} - \mu_{ti}}{\sqrt{\sigma_{ti}^2 + \epsilon}},
    \quad
    \mu_{ti} = \frac{1}{HW}\sum_{l=1}^W \sum_{m=1}^H x_{tilm},
    \quad
    \sigma_{ti}^2 = \frac{1}{HW}\sum_{l=1}^W \sum_{m=1}^H (x_{tilm} - mu_{ti})^2
$$
- This prevents instance-specific mean and [Covariance](Covariance.md) shift simplifying the learning process.
- Intuitively, the normalization process allows to remove instance-specific contrast information from the content image in a task like image stylization, which simplifies generation.
- ![](../images/Pasted%20image%2020221211131622.png)



