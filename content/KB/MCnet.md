---
toc: true
title: MCnet
tags: ['architecture']
---


## MCnet
- Encoder-Decoder Convolutional Neural Network and Convolutional LSTM for video prediction 
- two encoders, one is Content Encoder to capture the spatial layout of an image, and the other is Motion Encoder to model temporal dynamics within video clips. 
- The spatial features and temporal features are concatenated to feed to the decoder to generate the next frame 
- separately modeling temporal and spatial features, this model can effectively generate future frames recursively. 
- Videos consist of various lengths of frames which have rich spatial and temporal information 
- inherent temporal information within videos can be used as supervision signal for self-supervised feature learning 
- pretext tasks have been proposed by utilizing temporal context relations including temporal order verification [29], [40], [90] and temporal order recognition [27], [39]



