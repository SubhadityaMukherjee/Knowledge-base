---
toc: true
title: StarGAN
tags: ['architecture']
---


## StarGAN
- improve the scalability and robustness in handling more than two domains 
- builds only one model to perform image-to-image translation among multiply domains 
- In the generation phase, we just need to provide the generator with the source image and an attribute label which indicates the target domain 
- takes the domain label as an additional input and learns a deterministic mapping per each domain, which may result in the same output per each domain given an input image



