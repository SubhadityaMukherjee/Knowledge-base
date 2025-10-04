---
toc: true
title: Semantic Segmentation
tags: ['semisupervisedlearning']
---

## Semantic Segmentation
- task of assigning semantic labels to each pixel in images 
- autonomous driving, human-machine interaction, and robotic 
- Fully Convolutional Network (FCN) [4], DeepLab [5], PSPNet [6] and datasets such as PASCAL VOC [96], CityScape [97], ADE20K [98]. 
- FCN [4] is a milestone work for semantic segmentation since it started the era of applying fully convolution network (FCN) to solve this task 
- When using semantic segmentation as downstream task to evaluate the quality of image features learned by selfsupervised learning methods, the FCN is initialized with the parameters trained with the pretext task and fine-tuned on the semantic segmentation dataset, then the performance on the semantic segmentation task is evaluated and compared with that of other self-supervised methods.



