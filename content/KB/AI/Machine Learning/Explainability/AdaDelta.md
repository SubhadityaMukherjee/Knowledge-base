---
toc: true
title: AdaDelta

tags: ['gradients']
date modified: Monday, October 10th 2022, 2:02:35 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# AdaDelta
- $$RMS[\Delta \theta]_{t}= \sqrt{E[\Delta \theta^{2}]_{t}+ \epsilon}$$
$$\begin{align}\\
& \Delta \theta_{t}= -\frac{RMS[\Delta \theta]_{t-1}}{RMS[g]_{t}}g_{t}\\
& \theta_{t+1}= \theta_{t}+ \Delta \theta_{t}
\end{align}$$



