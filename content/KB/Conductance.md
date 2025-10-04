---
tags: ['explainabilitye-**02:35**explainability']
date created: Tuesday, January 10th 2023, 1:48:31 pm
date modified: Monday, January 16th 2023, 6:45:12 pm
---

# Conductance

- @dhamdhereHowImportantNeuron2018
- Kedar Dhamdhere, Mukund Sundararajan, Qiqi Yan

## Summary
- This paper introduces the concept of conductance as a way to understand the importance of hidden units in deep networks. Conductance is defined as the flow of [Integrated Gradients](Integrated Gradients.md)' attribution via a hidden unit, and is used to understand the importance of a hidden unit to the prediction for a specific input or over a set of inputs. The effectiveness of conductance is evaluated in multiple ways, including theoretical properties, ablation studies, and a feature selection task using the Inception network over ImageNet data and a sentiment analysis network over reviews. The properties of conductance include completeness, linearity and insensitivity to variations in inputs or hidden unit values. The paper also discusses the issue of saturation in neural networks, where the gradient of the output with respect to the input can be near-zero, and how conductance addresses this issue. The authors also compare conductance with other methods of understanding hidden unit importance and find it to be more intuitive and accurate.

## Abstract
- We introduce the notion of conductance to extend the notion of attribution to the understanding the importance of hidden units
- conductance of a hidden unit of a deep network is the flow of attribution via this hidden unit
- conductance to understand the importance of a hidden unit to the prediction for a specific input, or over a set of inputs
- We evaluate the effectiveness of conductance in multiple ways, including theoretical properties, ablation studies, and a feature selection task
- Inception network over ImageNet data, and a sentiment analysis network over reviews
- Informally, the conductance of a hidden unit of a deep network is the flow of [Integrated Gradients](Integrated Gradients.md)' attribution via this hidden unit
- The key idea behind conductance is to decompose the computation of [Integrated Gradients](Integrated Gradients.md) via the chain rule

## Conductance
- [Integrated Gradients](Integrated Gradients.md) produces attributions for base features
- There is a natural way to 'lift' these attributions to a neuron in a hidden layer. Consider a specific neuron y in a hidden layer of a network
- 
$$

F:R^{n} \rightarrow [0,1]
$$
 represents a deep network.
- $x \in R^{n}$ is input, $x' \in R^{n}$ is baseline input
- [Integrated Gradients](Integrated Gradients.md) is path integral of gradient along straightline path from baseline $x'$ to input $x$. The function F varies from a near zero value for the informationless baseline to its final value. The gradients of F with respect to the image pixels explain each step of the variation in the value of F
- The integration (sum) over the gradients cumulates these micro explanations and accounts for the net difference between the baseline prediction score (near zero) and the prediction value at the input x.
- $$
IG_{i}(x) ::== (x_{i}- x_{i}') \int_{\alpha=0}^{1} \frac{\partial F(x' + \alpha(x-x'))}{\partial x_{i}}d \alpha
$$ where $\frac{\partial F(x)}{\partial x_{i}}$ is grad of F along i^th dimension at x
- Conductance of neuron y for attribution to input variable i is $$
Cond_{i}^{y}(x) ::== (x_{i}- x_{i}') \int_{\alpha=0}^{1} \frac{\partial F(x' + \alpha(x-x'))}{\partial y} \cdot \frac{\partial y}{\partial x_{i}} d \alpha
$$

## Evaluation of Conductance
- Activation: The value of the hidden unit is the feature importance score.
- $Gradient\times Activation$ : $$
y \times \frac{\partial F(x' + \alpha \times (x-x'))}{\partial y} d \alpha
$$
- Internal Influence : $$
Int Inf ^{y}(x) ::= \int^{1}_{\alpha=0} \frac{\partial F(x' + \alpha(x-x'))}{\partial y} d \alpha
$$
- The premise is that hidden units that are important across a set of inputs from a class should be predictive of this input class.

## Properties of Conductance

### Completeness
- conductances for any single hidden layer add up to the difference between the predictions $F(x) - F(x')$
- conductances thus satisfy the [Layerwise Conservation Principle](Layerwise Conservation Principle.md)

### Linearity
- So do internal influence and gradient*activations
- Suppose that we linearly compose hidden neurons f1 and f2 to form the final network that models the function $a \times f_{1} + b \times f_{2}$. Then, the conductances of the two hidden neurons will be $a \times (f_{1}(x) f_{1}(x_{0}))$ and $b \times (f_{2}(x) f_{2}(x'))$ respectively.
- This is a sanity-check because if the action of a network is mostly linear from a hidden layer, the conductances will match what is intuitively the obvious solution.

### Insensitive
- If varying the values of a hidden unit does not change the network's prediction, it has zero conductance
- If varying the inputs does not change value of the hidden unit, the hidden unit has zero conductance
- Based on $\frac{\partial F}{\partial y_{j}}$ and $\frac{\partial y_{j}}{\partial x_{i}}$ being 0

## Saturation of Neural Networks
- Basically, for a network, or a sub-network, even when the output crucially depends on some input, the gradient of the output w.r.t. the input can be near-zero.
- As an artificial example, suppose the network first transforms the input x linearly to y = 2x, and then transforms it to z = max(y, 1). Suppose the input is x = 1 (where z is saturated at value 1), with 0 being the baseline. Then for the hidden unit of y, gradient of z w.r.t. y is 0. Gradient\*activation would be 0 for y, which does not reflect the intuitive importance of y. Like in [Integrated Gradients](Integrated Gradients.md), in computing conductance, we consider all extrapolated inputs for x between 0 and 1, and look at the gradients of output w.r.t. y at these points. This takes the non-saturated region into account, and ends up attributing 1 to y, as desired.
- wrong Polarity/Sensitivity

## Methods
- we compare against can yield scores that have signs and magnitudes that are intuitively incorrect
- This is intuitively because each misses terms/paths that our method considers.
- Activation values for a ReLU based network are always positive. However, ReLU nodes can have positive or negative influence on the output depending on the upstream weights. Here, Activation does not distinguish the sign of the influence, whereas condutance can.
- Gradient\*Activation as a linear projection can overshoot
- Certain hidden units that actually have near zero influence can be assigned high
- importance scores.
- For example, suppose that the network is the composition of two functions f (x) = x and a weighted ReLU g(y) = max(y 1, 0). Again, the network computes the composition g(f(x)). Suppose that the baseline is x = 0 and the input is x = 1 . The output of the network is 0. But the feature importance of the unit f is deemed to be 1 (activation) times 1 (gradient), which is 1 . Notice that this is the only unit in its layer, so the fact that its influence does not agree in magnitude with the output is undesirable. In contrast, conductance assigns all hidden units a score of zero. The example can be extended to show that the feature importance score can disagree in sign with the actual direction of influence.
- Suppose that the network is the composition two functions f(x) = x and g(y) = y, i.e., the network computes the composition g(f(x)). Suppose that the baseline is x = 0 and the input is x = 1. The output of the network is 1. But the internal influence of the unit represented by the function g is +1 (regardless of the choice of the input or the path). Notice that this is the only unit in
- its layer, so the fact that its influence does not agree in sign with the output is highly undesirable. In contrast, conductance assigns an influence score of 1.

## Applying Conductance to an Object Recognition Model
- We use conductance as a measure to identify influential filters in hidden layers in the Inception network.
- Given an input image, we identify the top predicted label
- For the pre-softmax score for this label, we compute the conductance for each of the filters in each of the hidden layers
- The [visualization](visualization.md) is done by aggregating the conductance along the color channel and scaling the pixels in the actual image by the conductance values.

## Ablation Study
- Next we studied how many filters we need to ablate in the network in order for the network to change its prediction. We found that, it is sufficient to ablate 3.7 on an average for the network to change its prediction for an image. Only 3 out of 100 images needed more than 10 filter ablations to change the predicted label. The maximum was 16. This provides further evidence that using conductance we can identify filters that are important for the prediction.
- We compare this to the filters with highest internal influence. Out of the 100 sample images, the network prediction changed for only 5 images when their top 10 filters

## Division of Labour
- We notice that almost all the filters either capture positive sentiment or negative sentiment, but not both.
- We substantiate via Figure 3, which is a clustered heatmap of signs of conductances of the 256 filters (columns) for around four thousand examples (rows) from the Stanford Sentiment Tree Bank [24]. Notice that very few filters have
- both negative and positive conductance. Negation
- Negation is commonly used in expressing sentiments, in phrases like "this is not good" or "this is not bad". Does the sentiment network understand negation? Does it have hidden units dedicated to implement the logic of negation? We first identify high conductance filters for the input "this is not good" that have a high attribution to the pattern "not good".
- Sentences with high conductance for filters that have high conductance for the phrase "not bad". These filters are largerly focussed on negation.

## Images
- ![](../images/Pasted%20image%2020230110140703.png)
- ![](../images/Pasted%20image%2020230110140713.png)
- ![](../images/Pasted%20image%2020230110140725.png)



