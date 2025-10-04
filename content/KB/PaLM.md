---
toc: true
title: PaLM

tags: ['architecture']
date modified: Monday, October 10th 2022, 2:02:20 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# PaLM
- [PaLM: Scaling Language Modeling with Pathways](https://arxiv.org/abs/2204.02311)
- single 540 billion parameter dense Transformer language model
- few-shot language understanding and generation
- drastically reduces the number of task-specific training examples needed to adapt the model to a particular application
- Pathways Language Model
- 6144 TPU v4 chips
- breakthrough performance on reasoning tasks, which require multi-step logical inference
- combination of scale and chain-of-thought prompting, where the model is explicitly prompted to generate a natural language logical inference chain before making its predictio
- write explicit logical inference chains to both explain jokes and answer complex questions about scenarios
- [Big-Bench](Big-Bench.md)
- suggest that the improvements from scale for few-shot language understanding have not yet plateaued
- When they compare results from PaLM 540B to our own identically trained 62B and 8B model variants, improvements are typically log-linear.
- certain capabilities of language models only emerge when trained at sufficient scale, and there are additional capabilities that could emerge from future generations of models
- demonstrating that prompting the model to generate explicit inference chains can drastically increase the quality of the predictions themselves
- model’s generation (rather than just understanding) capabilities can be immensely beneficial even for tasks that are modeled as categorical prediction or regression, which typically do not require significant language generation
- comprehensive analysis on bias and toxicity, and study the extent of training data memorization with respect to model scale
- ethical considerations related to large language models and discuss potential mitigation strategies



