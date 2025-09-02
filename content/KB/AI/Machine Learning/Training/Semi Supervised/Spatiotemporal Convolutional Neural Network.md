---
toc: true
title: Spatiotemporal Convolutional Neural Network
tags: ['semisupervisedlearning']
---

## Spatiotemporal Convolutional Neural Network
- 3D convolution operation was first proposed in 3DNet [62] for human action recognition 
- Compared to 2DConvNets which individually extract the spatial information of each frame and then fuse them together as video features, 3DConvNets are able to simultaneously extract both spatial and temporal features from multiple frames. 
- VGG-like 11-layer 3DConvNet designed for human action recognition 
- The network contains 8 convolutional layers, and 3 fully connected layers. All the kernels have the size of 3 x 3 x 3, the convolution stride is fixed to 1 pixel 
- The input of C3D is 16 consecutive RGB frames where the appearance and temporal cues from 16-frame clips are extracted 
- However, the paper of long-term temporal convolutions (LTC) [67] argues that, for # the long-lasting actions, 16 frames are insufficient to represent whole actions which last longer.



