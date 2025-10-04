---
toc: true
title: Image Generation with Colorization
tags: ['semisupervisedlearning']
---

## Image Generation with Colorization
- Image colorization is a task of predicting a plausible color version of the photograph given a gray-scale photograph as input 
- To correctly colorize each pixel, networks need to recognize objects and to group pixels of the same part together. Therefore, visual features can be learned in the process of accomplishing this task. 
- Zhang et al. proposed to handle the uncertainty by posting the task as a clas- sification task and used class-rebalancing to increase the diversity of predicted colors [18] 
- Some work specifically employs the image colorization task as the pretext for self- supervised image representation learning [18], [42], [82], [124] 
- After the image colorization training is finished, the features learned through the colorization process are specifically evaluated on other downstream high-level tasks with transfer learning.



