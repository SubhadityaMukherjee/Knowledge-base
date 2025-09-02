---
toc: true
title: LASER

tags: ['architecture']
date modified: Monday, October 10th 2022, 2:02:24 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# LASER
- [Massively Multilingual Sentence Embeddings for Zero-Shot Cross-Lingual Transfer and Beyond](https://arxiv.org/abs/1812.10464)
- joint multilingual sentence representations
- LASER
- Language-Agnostic SEntence Representations
- 93 languages, belonging to more than 30 different families and written in 28 different scripts
- universal language agnostic sentence embeddings
- train a single encoder to handle multiple languages, so that semantically similar sentences in different languages are close in the [Embedding](Embedding.md) space
- single BiLSTM encoder with a shared BPE vocabulary for all languages
- coupled with an auxiliary decoder and trained on publicly available parallel corpora
- learn a classifier on top of the resulting embeddings using English annotated data only, and transfer it to any of the 93 languages without any modification
- [XNLI](XNLI)
- [MLDoc](MLDoc.md)
- [BUCC](BUCC.md)
- test set of aligned sentences in 112 languages

# Laser
- Acronym for Light Amplification by Stimulated Emission of Radiation. A device that produces a coherent monochromatic beam of light which is extremely narrow and focused but still within the visible light spectrum. This is commonly used as a non-[Contact Sensor](Contact%20Sensor.md) for robots. Robotic applications include: distance finding, identifying accurate locations, surface mapping, bar code scanning, cutting, welding etc.



