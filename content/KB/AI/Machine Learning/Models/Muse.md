---
toc: true
title: Muse
tags: ['architecture']
---

## Muse
- Text-to-image transformer model
- state-ofthe-art image generation while being more ecient than difusion or autoregressive models
- it is trained on a masked modelling task in discrete token space
- more ecient because of the use of discrete tokens and requiring fewer sampling iterations
- parallel decoding
- Muse is 10x faster at inference time than Imagen-3B or Parti-3B and 3x faster than Stable Difusion v 1.4
- Muse is also faster than than Stable Difusion in spite of both models working in the latent space of a VQGAN



