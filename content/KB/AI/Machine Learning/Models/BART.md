---
toc: true
title: BART

tags: ['architecture']
date modified: Monday, October 10th 2022, 2:02:34 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# BART
- [BART: Denoising Sequence-to-Sequence Pre-training for Natural Language Generation, Translation, and Comprehension](https://arxiv.org/abs/1910.13461)
- [[Denoising Autoencoder]]
- pretraining sequence-to-sequence
- trained by corrupting text with an arbitrary noising function, and learning a model to reconstruct the original text
- generalizing BERT (due to the bidirectional encoder), [[GPT]] (with the left-to-right decoder),
- finding the best performance by both randomly shuffling the order of the original sentences and using a novel in-filling scheme, where spans of text are replaced with a single mask token
- With BERT, random tokens are replaced with masks, and the document is encoded bidirectionally. Missing tokens are predicted independently, so BERT cannot easily be used for generation.
- With [[GPT]], tokens are predicted auto-regressively (generation of a new token is conditioned on the prior tokens), meaning [[GPT]] can be used for generation.
- noising schemes to an input document and thus corrupts it by replacing spans of text with mask symbols
- effective when finetuned for text generation but also works well for comprehension tasks
- matches the performance of [[RoBERTa]] with comparable training resource
- [[GLUE]]
- [[SQuAD]]



