---
toc: true
title: AudioLM
tags: ['architecture']
---

## AudioLM
- maps the input audio into a sequence of discrete tokens and casts audio generation as language modeling task in this representation space
- training on large corpora of raw
- audio waveforms
- learns to generate natural and coherent continuations given short prompts
- extended beyond speech by generating coherent piano music continuations, despite being trained without any symbolic representation of music
- When it comes to audio synthesis, multiple scales make achieving high audio quality while displaying consistency very challenging
- This gets achieved by this model by combining recent advances in neural audio compression, self-supervised representation learning and language modelling.



