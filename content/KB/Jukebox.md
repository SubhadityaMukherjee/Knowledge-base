---
toc: true
title: Jukebox
tags: ['architecture']
---

## Jukebox
- generates music with singing in the raw audio domain
- earlier models in the text-to-music genre generated music symbolically in the form of a pianoroll which specifies timing, pitch and velocity.
- The challenging aspect is the non-symbolic approach where music is tried to be produced directly as a piece of audio
- the space of raw audio is extremely high dimensional which makes the problem very challenging
- the key issue is that modelling that raw audio produces long-range dependencies, making it computationally challenging to learn the high-level semantics of music.
- hierarchical VQ-VAE architecture to compress audio into a discrete space [14], with a loss function designed to retain the most amount of information.
- This model produces songs from very diferent genres such as rock, hip-hop and jazz.



