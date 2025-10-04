---
toc: true
title: ScoreCAM

tags: ['explainability']
date modified: Monday 20th February 2023, Mon
date created: Monday 20th February 2023, Mon
---

# ScoreCAM


- @wangScoreCAMScoreWeightedVisual2020
- In Score-Cam, we use the weights of the score obtained for a specific target class.
- The first step involved is passing images to a CNN model and performing a forward\_pass. After the forward pass, the activations are extracted from last convolutional layer in the network. 
- Each Activation Map obtained from the last layer having shape $1\times m \times n$ is then upsampled using bilinear-interpolation to the same size as the Input Image. 
- After Upsampling the activation maps, the resultant activation maps are normalized with each pixel within the range of \[0,1\] to maintain the relative intensities between the pixels 
	- $$A_{i,j}^{k}= \frac{A_{i,j}^{k}}{max A^{k}- min A^{k}}$$
- After the Normalization of the Activation Maps is complete, the highlighted areas of the activation maps are projected on the input space by multiplying each normalized activation map(1 x W x H) with the Original Input Image(3 x W x H) to obtain a masked image M with shape 3 x W x H
	- $$M^{k}= A^{k} \cdot I$$
- The Masked Images M thus obtained are then passed to Convolutional Neural Network with SoftMax output
	- $$S_{k} = Softmax(F(M^{k}))$$
- After getting the scores for each class we extract the score of the target class to represent the importance of the kth activation map.
	- $$w_{k}^{c}= S_{k}^{c}$$
- compute the sum across all the activation maps for the linear combination between the target class score and each activation map
- apply pixel-wise ReLU to the final activation map
	- $$L^{c}_{ScoreCAM} = ReLU(\underset{k}\Sigma w_{k}^{c}A^{k})$$
- ReLU because we are interested only in the features that have a positive influence on the class of interest

## Advantages

- can be used in any Convolutional Neural Network architecture and don't require retraining of the model to produce saliency maps like CAM
- class discriminative
- removes irrelevant noise to produce a meaningful saliency map
- Softmax scores as weights and removes the dependence on unstable gradients



