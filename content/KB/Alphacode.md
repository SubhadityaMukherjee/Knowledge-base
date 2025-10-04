---
toc: true
title: Alphacode
tags: ['architecture']
---

## Alphacode
- Other language models have demonstrated an impressive ability to generate code, but these systems still perform poorly when evaluated on more complex, unseen problems
- Alphacode is a system for code generation for problems that require for deeper reasoning
- having an extensive dataset for training and evaluation, large and ecient transformer based architectures and a large-scale model sampling.
- model is firstly pre-trained through GitHub repositories amounting to 715.1 GB of code.
- more extensive dataset than Codex's pre training dataset.
- For the training to be better, a fine-tuning dataset is introduced from the Codeforces plataform
- Codecontests are conducted, for the validation phase, in which we better the performance of the model.
- transformer-based architecture, they use an encoder-decoder transformer architecture
- Compared to decoder-only architectures commonly used, this architecture allows for a bidirectional description and extra flexibility.
- shallow encoder and a deep encoder to further the model's ecienc
- o reduce the cost of sampling, multi-query attention is used.



