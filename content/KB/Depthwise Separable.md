---
tags: ['temp']
toc: true
title: Depthwise Separable
date modified: Monday, October 10th 2022, 2:02:30 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# Depthwise Separable
- Only transforms the input once and saves computation -> elongate it to more channels
- From C -> F channels : Use F instances of a 1x1xC filter
- ![](../images/Pasted%20image%2020220306122226.png)



