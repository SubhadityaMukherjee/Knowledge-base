---
toc: true
title: Visual Context Augmentation
tags: ['augmentation']
date created: Sunday, October 9th 2022, 12:21:26 pm
date modified: Monday, October 10th 2022, 2:02:07 pm
---

# Visual Context Augmentation
- @dvornikModelingVisualContext2018
- learns to place object instances at an image location depending on the surrounding context.
- A neural network is trained for this purpose.
- The training data is pre- pared to generate a context image with the masked- out object inside it.
- From an image, 200 context sub-images are generated surrounding the blacked- out bounding box. The neural network learns to predict the category (object or background) in masked pixels.
- The object instances are placed inside the selected boxes to generate a new train- ing image



