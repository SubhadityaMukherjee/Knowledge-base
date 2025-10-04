---
toc: true
title: Phenaki
tags: ['architecture']
---

## Phenaki
- capable of performing realistic video synthesis, given a sequence of textual prompts
- Phenaki is the first model that can generate videos from open domain time variable prompts
- To address data issues, it performs joint training on a large image-text pairs dataset as well as a smaller number of video-text examples can result in generalization beyond what is available in the video datasets.
- image-text datasets having billions of inputs
- limitations come from computational capabilities for videos of variable length
- the C-ViViT encoder, the training transformer and the video generator
- The encoder gets a compressed representation of videos.
- First tokens are transformed into embeddings.
- This is followed by the temporal transformer, then the spatial transformer
- After the output of the spatial transformer, they apply a single linear projection without activation to map the tokens back to pixel space
- Consequently, the model generates temporally coherent and diverse videos conditioned on open domain prompts even when the prompt is a new composition of concepts



