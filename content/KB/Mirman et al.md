---
toc: true
title: Mirman et al.

tags: ['language']
date modified: Monday, October 10th 2022, 2:02:22 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# Mirman Et Al.
- train syllables in words, predicting the next syllable
- use network to train on different types of individual words, matching them with one of five objects, simulating word learning
- 75 epocs 1000 syllable sequence, then it predicted almost perfectly the next syllable (teaching phonotactics of the language)
- Model trained to recognize one of five objects for each of five different two-syllable input patterns of three types 1. words (100% transitional [Probability](Probability.md)) 2. partwords (25% [Probability](Probability.md) transitions) 3. nonwords (0% transitions)
- Model is better at mapping two-syllable sequences to words when it has already been exposed to those sequences and they had high probabilities
- Novel-sequence non-word labels initially learned nearly as fast as word up to intermediate point.
- exposure to familiarization input allowed network to created distinct hidden representations for each syllable
- [SRN](SRN.md) can show how statistical learning supports word learning, showing a link
- Humans are good at learning sequences, even when the data is presented implicitly and even when the relationships are non-adjacent
- We aren't just sensitive to frequency: we are sensitive to actual [Transitional probabilities](Transitional%20probabilities.md)
- SRNs with very simple assumptions model non-adjacent learning and [Transitional probabilities](Transitional%20probabilities.md)
- Biological arguments for distributed representations
- Makes more sense that neurons get randomly assigned to be active for different inputs
- We can start with randomness and with learning it will become structured
- concepts are just bundles of [Features](Features.md), that together become something
- Prevents catastrophic failures



