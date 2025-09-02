---
toc: true
title: CLIP

tags: ['architecture']
date modified: Monday, October 10th 2022, 2:02:32 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# CLIP
- [Learning Transferable Visual Models from Natural Language Supervision](https://arxiv.org/abs/2103.00020)
- introduces CLIP, a pre-training task which efficiently learns visual concepts from natural language supervision
- performs language-guided image generation
- uses vision and language encoders trained in isolation and uses a [[Contrastive Loss]] to bring similar image-text pairs closer, while pulling apart dissimilar pairs as a part of pretaining
- can be applied to any visual classification benchmark by simply providing the names of the visual categories to be recognized, similar to the “zero-shot” capabilities of [[GPT]] and [[GPT3]]
- pre-trains an image encoder and a text encoder to predict which images were paired with which texts in our dataset
- zero-shot classifier
- they convert all of a dataset’s classes into captions such as “a photo of a dog” and predict the class of the caption CLIP estimates best pairs with a given image





---
toc: true
title: CLIP
tags: ['architecture']
---

## CLIP
- is a neural network trained on a variety of (image, text) pairs
- Using CLIP, that can be instructed in natural language to predict the most relevant text snippet, given an image, the model has recently merged as a successful representation learner for images
- Concretely, CLIP embeddings have several desirable properties
- they are robust to image distribution shift, have impressive zero-shot capabilities and have been fine-tuned to achieve state-of-theart results
- the CLIP image embedding decoder module is combined with a prior model, which generates possible CLIP image embeddings from a given text caption



