---
toc: true
title: Object Detection
tags: ['semisupervisedlearning']
---

## Object Detection
- localizing the position of objects in images and recognizing the category of the objects 
- MSCOCO [99] and OpenImage [14] 
- When using object detection as downstream task to evaluate the quality of the self-supervised image features, networks that trained with the pretext task on unlabeled large data are served as the pre-trained model for the Fast-RCNN [2] and then fine-tuned on object detection datasets, then the performance on the object detection task is evaluated to demonstrate the generalization ability of self- supervised learned features.



