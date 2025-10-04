---
toc: true
title: Learning from Video Prediction
tags: ['semisupervisedlearning']
---


## Learning from Video Prediction
- Video prediction is a task of predicting future frame sequences based on a limited number of frames of a video 
- To predict future frames, network must learn the change in appearance within a given frame sequence 
- [Un-LSTM](Un-LSTM.md)
- [MCnet](MCnet.md)
- [Temporal order verification](Temporal order verification.md)
- [Temporal order recognition](Temporal order recognition.md)
- Misra et al. proposed to use the temporal order verification as the pretext task to learn image features from videos with 2DConvNet [40] which has two main steps: (1) The frames with significant motions are sampled from videos according to the magnitude of optical flow, (2) The sampled frames are shuffled and fed to the network which is trained to verify whether the input data is in correct order. 
- successfully verify the order of the input frames, the network is required to capture the subtle difference between the frames such as the movement of the person 
- semantic features can be learned through the process of accomplishing this task 
- the methods usually suffer from a massive dataset preparation step 
- The frame sequences that used to train the network are selected based on the magnitude of the optical flow, and the computation process of optical flow is expensive and slow



