---
toc: true
title: Learning from RGB-Flow Correspondence
tags: ['semisupervisedlearning']
---


## Learning from RGB-Flow Correspondence
- Optical flow encodes object motions between adjacent frames 
- RGB frames contain appearance information 
- The correspondence of the two types of data can be used to learn general features 
- This type of pretext tasks include optical flow estimation [151], [152] and RGB and optical flow correspondence verification [23]. 
- Sayed et al. proposed to learn video features by verifying whether the input RGB frames and the optical flow corresponding to each other 
- Two networks are employed while one is for extracting features from RGB input and another is for extracting features from optical flow input [24] 
- network needs to capture mutual information between the two modalities 
- mutual information across different modalities usually has higher semantic meaning compared to information which is modality specific 
- Optical flow estimation is another type of pretext tasks 
- [FlowNet](FlowNet.md)



