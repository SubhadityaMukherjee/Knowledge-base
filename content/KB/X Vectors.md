---
toc: true
title: X Vectors

tags: ['architecture']
date modified: Monday, October 10th 2022, 2:02:13 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# X Vectors
- [X-Vectors: Robust DNN Embeddings for Speaker Recognition](https://www.danielpovey.com/files/2018_icassp_xvectors.pdf)
- data [augmentation](Augmentation.md) to improve performance of deep neural network (DNN) embeddings for speaker recognition
- trained to discriminate between speakers, maps variable-length utterances to fixed-dimensional embeddings called x-vectors
- prior studies have found that embeddings leverage large-scale training datasets better than i-vectors, it can be challenging to collect substantial quantities of labeled data for training
- use data [augmentation](Augmentation.md), consisting of added noise and reverberation, as an inexpensive method to multiply the amount of training data and improve robustness
- Their data [augmentation](Augmentation.md) strategy employs additive noises and reverberation
- Reverberation involves convolving room [Impulse](Impulse.md) responses (RIR) with audio
- simulated RIRs described by [Ko et al.](https://danielpovey.com/files/2017_icassp_reverberation.pdf)
- reverberation itself is performed with the multicondition training tools in the Kaldi ASpIRE recipe
- For additive noise, they use the [MUSAN](MUSAN.md) dataset,
- PLDA classifier is used in the x-vector framework to make the final decision, similar to i-vector systems
- x-vectors are compared with i-vector baselines on [Speakers in the Wild](Speakers%20in%20the%20Wild.md) and [NIST SRE 2016 Cantonese](NIST%20SRE%202016%20Cantonese.md) where they achieve superior performance on the evaluation datasets



