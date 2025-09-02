---
toc: true
title: Conv Based Noise Reduction
tags: ['visualization']
date modified: Monday, October 10th 2022, 2:02:31 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# [Conv](Conv.md) Based Noise Reduction
- Noise is high frequency component, suppress via low-pass filters
- Ideal low-pass filter
- multiply with box filter in frequency domain
- convolution with sinc in spatial domain (impractical: infinite extent)
- ![](../images/Pasted%20image%2020220411130419.png)
- ![](../images/Pasted%20image%2020220411130431.png)
- Spatially narrow (wide) filter has wide (narrow) spectrum and low (high) smoothing effect



