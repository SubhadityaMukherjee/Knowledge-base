---
toc: true
title: Flamingo

tags: ['architecture']
date modified: Monday, October 10th 2022, 2:02:27 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# Flamingo
- [Flamingo: a Visual Language Model for Few-Shot Learning](https://arxiv.org/abs/2204.14198)
- large-scale pre-training followed by task-specific fine-tuning has emerged as a standard approach, but the fine-tuning step still requires a lot of samples.
- building models that can be rapidly adapted to numerous tasks using only a handful of annotated examples is an open challenge for multimodal machine learning research
- family of Visual Language Models (VLM) which seek to train a multi-modal model (i.e., with the ability to understand different types of input – visual, audio, text etc.) in a few-shot learning approach (which refers to the ability to learn a new task with just a few samples for training).
- bridge powerful pretrained vision-only and language-only models
- handle sequences of arbitrarily interleaved visual and textual data
- seamlessly ingest images or videos as inputs
- Interleave cross-attention [Layers](Layers.md) with language-only self-[Attention](Attention.md) [Layers](Layers.md) (frozen).
- Perceiver-based architecture that transforms the input sequence data (videos) into a fixed number of visual token
- Large-scale (web) multi-modal data by scraping webpages which has inter-leaved text and images
- Flamingo models can be trained on large-scale multimodal web corpora containing arbitrarily interleaved text and images, which is key to endow them with in-context few-shot learning capabilities





---
toc: true
title: Flamingo
tags: ['architecture']
---


## Flamingo
- A Visual Language Model created by Deepmind using few shot learning on a wide range of open-ended vision and language tasks, simply by being prompted with a few input/output examples
- the input of Flamingo contains visually conditioned autoregressive text generation models able to ingest a sequence of text tokens interleaved with images and/or videos
- and produce text as output
- A query is made to the model along with a photo or a video and the model answers with a text answer
- Flamingo models take advantage of two complementary models: a vision model that analyzes visual scenes and a large language model which performs a basic form of reasoning
- The language model is trained on a large amount of text data.



