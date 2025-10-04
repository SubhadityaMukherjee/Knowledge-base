---
toc: true
title: pGLSM

tags: ['architecture']
date modified: Monday, October 10th 2022, 2:02:10 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# pGLSM
- [Text-Free Prosody-Aware Generative Spoken Language Modeling](https://arxiv.org/abs/2109.03264)
- similar to how [GPT](GPT.md)-2 can generate coherent paragraphs
- builds upon [](https://aman.ai/papers/#generative-spoken-language-modeling-from-raw-audio)
- addresses the generative aspects of speech pre-training
- replacing text with discovered phone-like units for language modeling and shows the ability to generate meaningful novel sentences
- the units used in GSLM discard most of the prosodic information
- fails to leverage prosody for better comprehension, and does not generate expressive speech
- prosody-aware generative spoken language model (pGSLM)
- multi-stream transformer language model (MS-TLM) of speech, represented as discovered unit and prosodic feature streams, and an adapted HiFi-GAN model converting MS-TLM outputs to waveform



