---
toc: true
title: Chinchilla

tags: ['architecture']
date modified: Monday, October 10th 2022, 2:02:31 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# Chinchilla
- [Training Compute-Optimal Large Language Models](https://arxiv.org/abs/2203.15556)
- given a 10x increase in computational budget, model size should increase 5.5x, and the number of tokens should only increase 1.8x
- model and data size should increase in accordance
- collecting high-quality datasets will play a key role in further scaling of LLMs
- optimal model size and number of tokens for training a [[Transformer]] [[language]] model under a given compute budget
- By training over 400 language models ranging from 70 million to over 16 billion parameters on 5 to 500 billion tokens, they find that for compute-optimal training, the model size and the number of training tokens should be scaled equally: for every doubling of model size the number of training tokens should also be doubled
- significantly outperforms Gopher (280B), [[GPT]]-3 (175B), Jurassic-1 (178B), and Megatron-Turing NLG (530B) on a large range of downstream evaluation tasks
- ubstantially less compute for fine-tuning and inference, greatly facilitating downstream usage
- [[MMLU]]



