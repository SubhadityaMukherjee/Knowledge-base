---
tags: ['temp']
date modified: Monday, October 10th 2022, 2:02:22 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

---

toc: true
title: MoCO

tags: ['temp']

---

# MoCO
- [Momentum Contrast for Unsupervised Visual Representation Learning](https://arxiv.org/abs/1911.05722)
- unsupervised visual representation learning
- contrastive learning as dictionary look-up, MoCo builds a dynamic dictionary with a queue and a moving-averaged encoder
- large and consistent dictionary on-the-fly
- [ImageNet](ImageNet.md)
- transfer well to downstream tasks.
- [PASCAL VOC](PASCAL%20VOC.md)
- [COCO](COCO.md)
- visual representation encoder by matching an encoded query
- to a dictionary of encoded keys using a [Contrastive Loss](Contrastive%20Loss.md)
- dictionary is built as a queue, with the current mini-batch enqueued
- oldest mini-batch dequeued
- slowly progressing encoder
- momentum update with the query encoder
- ![](../images/moco1.jpg)
- ![](../images/moco2.jpg)



