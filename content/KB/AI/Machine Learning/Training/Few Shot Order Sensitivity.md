---
toc: true
title: Few Shot Order Sensitivity

tags: ['temp']
date modified: Monday, October 10th 2022, 2:02:27 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# Few Shot Order [Sensitivity](Sensitivity.md)
- [Fantastically Ordered Prompts and Where to Find Them: Overcoming Few-Shot Prompt Order Sensitivity](https://arxiv.org/abs/2104.08786)
- When primed with only a handful of training samples, very large, pretrained language models such as [GPT](GPT.md)-3 have shown competitive results when compared to fully-supervised, fine-tuned, large, pretrained language models
- few-shot prompts suffer from order [Sensitivity](Sensitivity.md)
- for the same prompt the order in which samples are provided can make the difference between state-of-the-art and random performance – essentially some permutations are “fantastic” and some not
- problem is prevalent across tasks, model sizes (even for the largest current models), prompt templates, it is not related to a specific subset of samples, number of training samples, and that a given good permutation for one model is not transferable to another.
- novel probing method that exploits the generative nature of language models to construct an artificial development set
- identity performant permutations for prompts using [Entropy](Entropy.md)-based statistics over this set, which yields a 13% relative improvement for [GPT](GPT.md)-family models across eleven different established text classification tasks



