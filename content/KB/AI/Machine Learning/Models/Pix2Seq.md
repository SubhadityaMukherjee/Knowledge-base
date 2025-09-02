---
toc: true
title: Pix2Seq

tags: ['architecture']
date modified: Monday, October 10th 2022, 2:02:19 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# Pix2Seq
- [Pix2seq: a Language Modeling Framework for Object Detection](https://arxiv.org/abs/2109.10852)
- generic framework for object detection
- object detection as a language modeling task conditioned on the observed pixel inputs
- Object descriptions (e.g., bounding boxes and class labels) are expressed as sequences of discrete tokens, and we train a neural network to perceive the image and generate the desired sequence
- [COCO](COCO.md)
- output can be represented by a relatively concise sequence of discrete tokens (e.g., keypoint detection, image captioning, visual question answering)
- [Autoregressive](Autoregressive.md)
- stop inference when the ending token is produced
- applying it to offline inference, or online scenarios where the objects of interest are relatively sparse
- entirely based on human annotation



