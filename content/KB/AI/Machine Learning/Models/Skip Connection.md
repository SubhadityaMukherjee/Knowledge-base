---
tags: ['temp']
toc: true
title: Skip Connection
tag: architecture
date modified: Monday, October 10th 2022, 2:02:16 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# Skip Connection
- ![](../images/Pasted%20image%2020220306120520.png)
- $$x_i = F(x_{i-1}) + x_{i-1}$$
- [Effect Of Depth](Effect%20Of%20Depth.md)
- Previous layer gradient carried to next module untouched -> [loss](../Tag%20Pages/loss.md) surface is smoother
- Transfer #architecture to prevent [Vanishingexploding gradients](Vanishingexploding%20gradients.md)
- Learns the difference (residual) $$F(x) = H(x)-x$$



