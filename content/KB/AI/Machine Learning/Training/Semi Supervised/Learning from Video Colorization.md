---
toc: true
title: Learning from Video Colorization
tags: ['semisupervisedlearning']
---

## Learning from Video Colorization
- Temporal coherence 
- consecutive frames within a short time have similar coherent appearance 
- The coherence of color can be used to design pretext tasks for self-supervised learning 
- One way to utilize color coherence is to use video colorization as a pretext task for self-supervised video feature learning. 
- Video colorization is a task to colorize gray-scale frames into colorful frames 
- Vondrick et al. proposed to constrain colorization models to solve video colorization by learning to copy colors from a reference frame 
- Given the reference RGB frame and a gray-scale image, the network needs to learn the internal connection between the reference RGB frame and gray-scale image to colorize it. 
- tackle video colorization by employing a fully convolution neural network 
- Tran et al. proposed an U-shape convolution neural network for video colorization [160] 
- The color coherence in videos is a strong supervision signal



