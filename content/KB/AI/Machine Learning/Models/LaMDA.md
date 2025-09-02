---
toc: true
title: LaMDA
tags: ['architecture']
---

## LaMDA
- language model for dialog applications
- family of transformer-based neural language models specialized for dialog which have up to 137B parameters and are pre-trained on 1.56T words of public dialog data and web text.
- Fine-tuning can enable for safety and factual grounding of the model
- Only 0.001% of training data was used for fine-tuning, which is a great achievement of the model
- dialog modes take advantage of Transformers' ability to present long-term dependencies in text
- generally very well-suited for model scaling
- use of a single model to perform multiple tasks: it generates several responses, which are filtered for safety, grounded on an external knowledge source and reranked to find the highest-quality response.



