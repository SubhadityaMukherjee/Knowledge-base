---
toc: true
title: GradCAM

tags: ['architecture']
date modified: Saturday, January 14th 2023, 4:45:37 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# GradCAM
- @selvarajuGradCAMVisualExplanations
- Modified [CAM](CAM.md)
- Importance of feature map k for target class c
	- A is input
	- $Y_{c}=\text{score of class c}$ : value of output before softmax
	- grad of $Y_{c}$ wrt A and take avg
	- 
$$

\alpha_{k}^{c}= average(\partial \frac{Y_{c}}{\partial A^{k}_{ij}})
$$
	- If avg is high : important
	- 0 : not
	- neg : background/ others
- Weighted combination -> relu
	- $$
L^{c}_{GRADCAM}=Resize(ReLU(\Sigma_{k}(\alpha^{c}_{k}A^{k})))
$$
	- This is a coarse heatmap because the image is resized
	- ReLU used because we only care about positive values (actualy image pixel)
- To identify [Counterfactual Images](Counterfactual Images.md), flip the signs
	- 
$$

\alpha_{k}^{c}=average(- \partial \frac{Y_{c}}{\partial A^{k}_{ij}})

$$
	- ![](images/Pasted%20image%2020221118132132.png)
- Followed by [Guided GradCAM](Guided GradCAM.md)

## Other Stuff
- producing ‘visual explanations’ for decisions from a large class of CNN-based models, making them more transparent and explainable
- Gradient-weighted Class Activation Mapping
- uses the gradients of any target concept
- flowing into the final convolutional layer to produce a coarse localization map highlighting the important regions in the image for predicting the concept
- lend insights into failure modes of these models (showing that seemingly unreasonable predictions have reasonable explanations)
- are robust to adversarial perturbations
- are more faithful to the underlying model
- help achieve model generalization by identifying dataset bias
- identify important neurons through GradCAM and combine it with neuron names to provide textual explanations for model decisions

## GradCAM Vs CAM
- Gradient-weighted Class Activation Mapping (Grad-CAM) is an improvement over Class Activation Mapping ([CAM]) that provides a more detailed and accurate [visualization](CAM]) that provides a more detailed and accurate [visualization.md) of the regions of an image that are important for a given classification.
- [CAM](CAM.md) generates heatmaps by using global average pooling (GAP) in the final convolutional layer to generate a feature map, followed by a linear combination of the feature map and the class weight vector to generate a single class activation map. However, this approach does not take into account the gradients of the class scores with respect to the feature maps, which can provide additional information about the contribution of different regions of the image to the final classification decision.
- Grad-CAM, on the other hand, uses the gradients of the class scores with respect to the feature maps in order to generate heatmaps. Specifically, it uses the gradients of the class scores with respect to the final feature maps of the network, which are then upsampled to the same size as the input image. The resulting heatmap highlights the regions of the input image that are most important for the given classification.
- In summary, Grad-CAM is an improvement over CAM because it provides a more detailed and accurate [visualization](visualization.md) of the regions of an image that are important for a given classification by using gradients of the class scores with respect to the feature maps, providing additional information about the contribution of different regions of the image to the final classification decision.



