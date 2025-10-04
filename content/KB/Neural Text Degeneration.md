---
toc: true
title: Neural Text Degeneration

tags: ['architecture']
date modified: Monday, October 10th 2022, 2:02:21 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# Neural Text Degeneration
- [The Curious Case of Neural Text Degeneration](https://arxiv.org/abs/1904.09751)
- deep analysis into the properties of the most common decoding methods for open-ended language generation
- surprising distributional differences between human text and machine text
- decoding strategies alone can dramatically effect the quality of machine text, even when generated from exactly the same neural language model
- likelihood maximizing decoding causes repetition and overly generic language usage
- sampling methods without truncation risk sampling from the low-confidence tail of a model’s predicted distribution
- [Nucleus Sampling](Nucleus%20Sampling.md)



