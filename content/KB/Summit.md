---
toc: true
title: Summit

tags: ['explainability']
date modified: Wednesday, October 12th 2022, 4:44:49 pm
date created: Wednesday, October 12th 2022, 4:44:48 pm
---

# Summit

- @hohmanSummitScalingDeep2019
- combines two scalable tools: (1) activation aggregation discovers important neurons; (2) neuron-influenced aggregation identifies relationships among such neurons. An attribution graph that reveals and summarizes crucial neuron associations and substructures that contribute to a model's outcomes is created. Summit combines famous methods such as computing synthetic prototypes of features and showing examples from the dataset that maximize special neurons of different layers. Deeper in the graph, it is examined how the low-level features combine to create high-level features. Novel as well is that it exploits neural networks with activation atlases [63]
- This method uses feature inversion to visualize millions of activations from an image classification network to create an explorable activation atlas of features the network has learned. Their approach is able to reveal visual abstractions within a model and even high-level misunderstandings in a model that can be exploited. Activation atlases are a novel way to peer into convolutional vision networks and represents a global, hierarchical, and human-interpretable overview of concepts within the hidden layers.
- To quantify how much a layer influences the next, the authors aggregate the influences by creating a tensor $I^{l}$ for all the layers of the network ($l$). How important channel $i$ of the layer $l-1$ is determined by the aggregate tensor $I^{l}_{cij}$ where $j$ represents the output channel and $c$ is the class of the image. Considering the $j^{th}$ kernel of the layer $K^{(j)} \in \mathbb{R}^{H \times W \times C_{l-1}}$, a single channel $Y$ can be represented using the 3D convolution operation by $Y_{:,:,j}= X \ast K^{(j)}$. This is equivalent to it's representation by the 2D convolution $Y_{:,:,j}= \Sigma_{i=1}^{C_{l-1}} X_{:,:,i} \ast K^{(j)}_{:,:,i}$. 
- $X_{:,:,i} \ast K^{(j)}_{:,:,i}$ is the contribution of the current channel from the previous layer and the maximum of this value is used to generate the influence map.



