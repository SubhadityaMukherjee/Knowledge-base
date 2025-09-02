---
toc: true
title: Inception
tags: ['architecture']
date modified: Monday, October 10th 2022, 2:02:25 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# Inception
- @szegedyGoingDeeperConvolutions2014
- [Rethinking the Inception Architecture for Computer Vision](https://arxiv.org/abs/1512.00567)

### V1
- [Conv](Conv.md) at different filter scales to find different kinds of [Features](Features.md) -> stack them up
- Increasing both the depth and width of the network while keeping computations at a manageable level
- Human visual system wherein information is processed at multiple scales and then aggregated locally
- channel [Dimensionality Reduction](Dimensionality%20Reduction.md), by reducing the output channels of the input
- To enable concatenation of [Features](Features.md) convolved with different kernels, they pad the output to make it the same size as the input.
	- without dilation
	- padding $p = (k-1)/2p$
	- since $out = in +2p -k +1$
- ![](../images/Pasted%20image%2020220306120214.png)

### V2/V3
- nxn [Conv](Conv.md) -> 1xn followed by nx1 [Conv](Conv.md)
- 5x5, 7x7 -> 2 and three 3x3 seq [Conv](Conv.md)
- More filters (wider)
- Distributed the computational budget in a balanced way between the depth and width of the network
- Added [Batch Normalization](Batch%20Normalization.md)
- ![](../images/Pasted%20image%2020220306121513.png)

## V4
- ([from](https://publish.obsidian.md/fabian-groeger/Machine+Learning+%26+Deep+Learning/Deep+Learning/Architectures/CNN/Inception-v4))
Paper: [https://arxiv.org/pdf/1602.07261.pdf](https://arxiv.org/pdf/1602.07261.pdf)  
Year: 2016  
Summary: New Residual [Inception](Inception.md) Architecture (deep [CNN](https://publish.obsidian.md/fabian-groeger/Machine+Learning+%26+Deep+Learning/Deep+Learning/Architectures/CNN/CNN))
- Why?
    - Introduction of residual connections on traditional architectures yielded SOTA performance (2015)
- Research question
    - Are there benefits when combining residual connections with the Inception architecture?
- Findings
    - Residual connections accelerates training of the Inception architecture
    - Residual Inception outperforming similar architecture only close
    - When the number of filters were higher than 1′000 the residual variants of the network died early in the training (e.g. outputted only zeros)
        - was not able to fix with lowering the Learning Rate or [Batch Normalization](Batch%20Normalization.md)
    - Scaling down the residuals before adding them with the residual connection stabilized the training (factor: 0.1−0.3)
- General Ideas
    - **Parallel convolutions**: Similar to the GoogLeNet architecture within their _modules_ the authors simultaneously use multiple convolutional branches with different [Receptive field](Receptive%20field.md) sizes on the same input activation maps and again concatenate those activations for further processing.
    - **Reduction modules**: Instead of simply applying a single max pooling or a 2-stride convolution to downsize the spatial dimensions, the authors dedicated whole modules to this task again employing parallel branches. 
    - **Strong usage of small convolutional kernels**(e.g. 3×3): Throughout the network the authors pefer smaller convolutional kernel size over larger ones, as this enables the same [Receptive field](Receptive%20field.md) with less parameters (e.g. a single 5×5convolution [Receptive field](Receptive%20field.md) as 2 consecutive 3×3convolutions [∼18 params ], but the later has less parameters)
    - **Factorization of convolutions**: They factorize convolutions of filter size n×n to a combination of 1×n and n×1 convolutions, in order to reduce the nr of parameters even further (e.g. 7×7 [∼49 params ] results in 1×7 and 7×1 [∼14 params ]!)
    - **Residual connections**: In the `Inception-ResNet-v1` and `Inception-ResNet-v2` the authors employ the usage of residual connections. Although the residual version of the networks converge faster, the final accuracy seems to mainly depend on the model size.
    - **Usage of bottleneck layers**: In order to reduce the cost of the individual convolutional branches within their modules, they apply 1×1convolutions at the beginning to reduce the depth of the input activation maps.
- Remarks
    - Authors disagree with residual paper one some points 
        - Residual connections are nessecary for training deep convolutional models
            - They show that it is not hard to train very deep models which achieve high performance without residual connections
            - They argue that residual connections do only speed up the training greatly
        - "Warm up" phases (pre-training with very low LR followed by a high LR) do not help to stabilize training very deep networks
            - high LR had the chance to destroy already learnt features
            - Scaling should be used instead



