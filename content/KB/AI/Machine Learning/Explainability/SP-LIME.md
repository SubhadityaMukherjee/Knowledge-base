---
toc: true
title: SP-LIME

tags: ['explainability']
date modified: Wednesday, October 12th 2022, 4:44:08 pm
date created: Wednesday, October 12th 2022, 4:44:07 pm
---

# SP-LIME
- @ribeiroWhyShouldTrust2016a

- model judges whether you can trust the whole model or not. It selects a picked diverse set of representative instances with LIMEs via submodular optimization. The user should evaluate the black box by regarding the feature words of the selected instances. It is conceivable that it also recognizes bias or systematic susceptibility to adversarial examples. With this knowledge, it is also possible to improve a bad model. SP-LIME was researched with text data, but the authors claimed that it can be transferred to models for any data type.
- This was inspired by CAM and [Grad-CAM](Grad-CAM.md) and tested the explanator on randomly chosen images from the COCO dataset [91], applied to the pre-trained neural network VGG-16 using the Kullback–Leibler (KL) divergence



