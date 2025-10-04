---
toc: true
title: Ego-motion
tags: ['semisupervisedlearning']
---


## Ego-motion
- self-driving car 
- equipped with various sensors 
- large-scale egocentric video along with ego-motor signal can be easily collected with very low cost by driving the car in the street 
- the correspondence between visual signal and motor signal for self-supervised feature learning 
- correspondence between visual signal and motor signal for s 
- underline intuition of this type of methods is that a self-driving car can be treated as a camera moving in a scene 
- egomotion of the visual data captured by the camera is as same as that of the car 
- correspondence between visual data and egomotion can be utilized for self- supervised feature learning 
- inputs to the network are two frames sampled from an egocentric video within a short time 
- labels for the network indicate the rotation and translation relation between the two sampled images which can be derived from the odometry data of the dataset. 
- ConvNet is forced to identify visual elements that are present in both sampled images. 
- ego-motor signal is a type of accurate supervision signal 
- In addition to directly applying it for self-supervised feature learning, it has also been used for unsupervised learning of depth and ego-motion



