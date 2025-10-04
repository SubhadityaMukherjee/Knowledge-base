---
toc: true
title: Data aug for spoken language

tags: ['temp']
date modified: Monday, October 10th 2022, 2:02:30 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# Data Aug for Spoken Language
- [Comparing Data Augmentation and Annotation Standardization to Improve End-to-end Spoken Language Understanding Models](https://assets.amazon.science/a5/65/cb86affe4903b5d6e55743fb23a1/comparing-data-augmentation-and-annotation-standardization-to-improve-end-to-end-spoken-language-understanding-models.pdf)
- All-neural end-to-end (E2E) Spoken Language Understanding (SLU) models can improve performance over traditional compositional SLU models, but have the challenge of requiring high-quality training data with both audio and annotations
- they struggle with performance on “golden utterances”, which are essential for defining and supporting [Features](Features.md), but may lack sufficient training data
- using data [augmentation](Augmentation.md) to compare two data-centric AI methods to improve performance on golden utterances
- improving the annotation quality of existing training utterances and augmenting the training data with varying amounts of synthetic data
- both data-centric approaches to improving E2E SLU achieved the desired effect, although data [augmentation](Augmentation.md) was much more powerful than annotation standardization.
- leads to improvement in intent recognition error rate (IRER) on their golden utterance test set by 93% relative to the baseline without seeing a negative impact on other test metrics



