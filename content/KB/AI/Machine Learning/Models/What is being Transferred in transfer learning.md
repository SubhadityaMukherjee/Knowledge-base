---
toc: true
title: What is being Transferred in transfer learning

tags: ['explainability']
date modified: Monday 27th February 2023, Mon
date created: Monday 27th February 2023, Mon
---

# What is being Transferred in transfer learning
- @neyshaburWhatBeingTransferred2020

## Abstract
- desired capability for machines is the ability to transfer their knowledge of one domain to another where data is (usually) scarce
- what enables a successful transfer and which part of the network is responsible for tha
- series of analyses on transferring to block-shuffled images, we separate the effect of feature reuse from learning low-level statistics of data and show that some benefit of transfer learning comes from the latter when training from pre-trained weights, the model stays in the same basin in the loss landscape and different instances of such model are similar in feature space and close in parameter space

## Main contributions and takeaways
- For a successful transfer both feature-reuse and low-level statistics of the data are important.
- Models trained from pre-trained weights make similar mistakes on target domain, have similar features and are surprisingly close in distance in the parameter space
- hey are in the same basins of the loss landscape models trained from random [Initialization](Initialization.md) do not live in the same basin, make different mistakes, have different features and are farther away in 2 distance in the parameter space
- Modules in the lower layers are in charge of general features and modules in higher layers are more sensitive to perturbation of their parameters.
- T: trained, P: Pre-trained, RI: random [Initialization](Initialization.md). Therefore we use the following abbreviations for the four models throughout the paper: RI (random [Initialization](Initialization.md)), P (pre-trained model), RI-T (model trained on target domain from random [Initialization](Initialization.md)), P-T (model trained/fine-tuned on target domain starting from pre-trained weights) 
- IMAGENET 
- CHEXPERT
- DOMAINNET

## What is being transferred

## Role of feature reuse
- Human visual system is compositional and hierarchical: neurons in the primary visual cortex (V1) respond to low level features like edges, while upper level neurons (e.g. the grandmother cell [Gross, 2002]) respond to complex semantic inputs Modern convolutional neural networks trained on large scale visual data are shown to form similar feature hierarchies [Bau et al., 2017, Girshick et al., 2014] The benefits of transfer learning are generally believed to come from reusing the pre-trained feature hierarchy useful when the downstream tasks are too small or not diverse enough to learn good feature representations
- create a series of modified downstream tasks which are increasingly distant from normal visual domains In particular, we partition the image of the downstream tasks into equal sized blocks and shuffle the blocks randomly The shuffling disrupts high level visual features in those images but keeps the low level statistics about the pixel values intact The extreme case of block size 224 x 224 means no shuffling; in the other extreme case, all the pixels in the image are shuffled, making any of the learned visual features in
- pre-training completely useless
- We conclude that feature reuse plays a very important role in transfer learning, especially when the downstream task shares similar visual features with the pre-training domain. But there are other factors at play: in these experiments we change the size of the shuffled blocks all the way to 1 and even try shuffling the channels of the input, therefore, the only object that is preserved here is the set of all pixel values which can be treated as a histogram/distribution We refer to those information as low-level statistics, to suggest that they are void of visual/semantic structural information. The low-level statistics lead to significant benefits of transfer learning, especially on optimization speed.
- We observe that two instances of P-T are highly similar across different layers. owever, between P-T and RIT instance or two RI-T instances, the similarity is very low. feature similarity is much stronger in the penultimate layer than any earlier layers both between P-T and RI-T instance and two RI-T instances, however, still an order of magnitude smaller than similarity between two P-T layers.
- These experiments show that the [Initialization](Initialization.md) point, whether pre-trained or random, drastically impacts feature similarity, and although both networks are showing high accuracy, they are not that similar in the feature space. two P-T are reusing the same features
- Distance in parameter space istance between two models in the parameter space More specifically, we measure the `L2` distance between 2 P-Ts and 2 RI-Ts, both per module and for the entire network Interestingly, RI-Ts are farther from each other compared to two P-Ts
- distance between modules increases as we move towards higher layers in the network.

## Performance barriers and basins in the loss landscape
- A commonly used criterion for better generalization performance is the flatness of the basin of the loss landscape near the final solution. In a flat basin, the weights could be locally perturbed without hurting the performance, while in a narrow basin, moving away from the minimizer would quickly hit a barrier, indicated by a sudden increase in the loss.
- We evaluate a series of models along the linear interpolation of the two weights { 2 } any two minimizers of a deep network can be connected via a non-linear low-loss path Garipov et al. [2018], Draxler et al. [2018], Fort and Jastrzebski [2019] n contrast, due to the non-linear and compositional structure of neural networks, the linear combination of the weights of two good performing models does not necessarily define a well behaved model, thus performance barriers are generally expected along the linear interpolation path owever, in the case when the two solutions belong to the same flat basin of the loss landscape, the linear interpolation remains in the basin As a result, a performance barrier is absent interpolating two random solutions from the same basin could generally produce solutions closer to the center of the basin, which potentially have better generalization performance than the end points
- we require that for most points on the basin, their convex combination is on the basin as well. This extra constraint would allow us to have multiple basins that may or may not be connected though a low-loss (nonlinear) path.
- Given a loss function $l: \mathcal{R}^{n} \rightarrow \mathcal{R}^{+}$, closed convex set $S \subset \mathcal{R}^{n}$, S is a $(\epsilon , \delta)$ basin for l iff S has the following properties
	- Let $U_S$ be the uniform distribution over set S and $\mu_{S,l}$ be the expected value of the loss on samples generated from $U_S$. Then,
		- $$\mathcal{E}_{w \sim U_{S}}[|\mathcal{l}(w)-\mu_{S, \mathcal{l}}] \leq \epsilon$$
	- For any two points $w_{1}, w_{2} \in S$, let $f(w_{1}, w_{2}) = w_{1}+ \overset{\sim}\alpha(w_{2}-w_{1})$ where $\overset{\sim}\alpha = max\{\alpha|w_{1}+ \alpha(w_{2}-w_{1})\}$
		- $$\mathcal{E}_{w_{1}, w_{2} \sim U_{S}, v \sim \mathcal{N}(0, \frac{\delta^{2}}{n}I_{n})}[\mathcal{l}(f(w_{1}, w_{2})+v )- \mu_{S,l}] \geq 2 \epsilon$$
	- Let $\kappa(w_{1}, w_{2}, v) = f(w_{1}, w_{2})+ \frac{v}{||f(w_{1}, w_{2})-w_{1}||}(f(w_{1}, w_{2})-w_{1})$. Then,
		- $$\mathcal{E}_{w_{1}, w_{2} \sim U_{S}, v \sim \mathcal{N}(0,\delta^{2})}[\mathcal{l}(\kappa(w_{1}, w_{2}, |v|))-\mu_{S,l}] \geq 2 \epsilon$$
- there are three requirements for a convex set to be a basin The first requirement is that for most points on the basin, their loss should be close to the expected value of the loss in the basin. This notion is very similar to requiring the loss to have low variance for points on the basin4. The last two requirements ensure that the loss of points in the vicinity of the basin is higher than the expected loss on the basin. In particular, the
- second requirement does that by adding Gaussian noise to the points in the basin and requiring the loss to be higher than the expected loss in the basin. The third requirement does something similar along the subspaces spanned by extrapolating the points in the basin. That is, if one exits the basin by extrapolating two points on the basin, the loss should increase.
- Starting with the two P-T solutions, we extrapolated beyond their connecting intervals to find the basin boundary, and calculated the parameters according to Definition 3.1. We found that each pair of P-T solutions live in a (0.0038, 49.14)-basin, (0.0054, 98.28)-basin and (0.0034, 49.14)-basin for rea, cipart and quickdraw, respectively

## Module Criticality
- Given $e > 0$ and network $f_\Theta$ ,
	- $$\mu_{i, \epsilon}(f_{\Theta})= \underset{0 \leq \alpha_{i}, \sigma_{i} \leq 1}{min}{\frac{\alpha_{i}^{2}||\theta_{i}^{F}-\theta_{i}^{0}||^{2}_{Fr}}{\sigma_{i}^{2}}}:\{ \mathbb{E}_{u \sim \mathcal{N}(0, \sigma_{i}^{2})}[\mathcal{L}_{S}(f_{\theta_{i}^{\alpha}}+u,\Theta_{-i}^{F})] \leq \epsilon \}$$
- different layers of the network show different robustness to perturbation of their weight values [Zhang et al., 2019a]
- They noted that for some modules, which they called critical, the performance of the model drops significantly after rewinding, while for others the performance is not impacted
- Module criticality is a measure that can be calculated for each module and captures how critical each module is.
- module criticality captures the role of the module in the generalization performance of the whole architecture and can be used as a measure of capacity of the module and predict the generalization performance we extend the definition of module criticality by looking at both direct path that linearly connect the initial and final value of the module and the optimization path generated by an optimizer from [Initialization](Initialization.md) to the final solution
- We also look into the final value of a weight matrix in addition to its optimal value during training as the start point of the path for investigating criticality
- We note a similar pattern as observed in the supervised case. The only difference is that the 'FC' layer becomes critical for P-T model, which is expected.

## Which pre-trained checkpoint is most useful for transfer learning?
- independence between the improvements on optimization speed and final performance. Moreover, this is in line with the loss landscape observations in Section 3.3. Earlier checkpoints in pre-training are out of basin of the converged model and at some point during training we enter the basin (which is the same for pre-train and fine-tune models
- This also explains the plateau of performance after some checkpoints. herefore, we can start from earlier
- checkpoints in pre-training.

## Conclusion
- We investigated the role of feature reuse through shuffling the blocks of input and showed that when trained from pre-trained weights [Initialization](Initialization.md), the network stays in the same basin of the solution, features are similar and models are close in the L2 distance in parameter space confirmed that lower layers are in charge of more general features
- one can use top singular values and directions for each module for [Initialization](Initialization.md) and investigate if this suffices for good transfer, or ensure [Initialization](Initialization.md) at the same basin but adding randomization to enhance diversity and improve generalization
- taking model average of models in the same basin does not disturb the performance

## Images
- ![](../images/Pasted%20image%2020230306145203.png)
- ![](../images/Pasted%20image%2020230306145307.png)
- ![](../images/Pasted%20image%2020230306145327.png)
- ![](../images/Pasted%20image%2020230306145335.png)
- ![](../images/Pasted%20image%2020230306145355.png)
- ![](../images/Pasted%20image%2020230306145405.png)
- ![](../images/Pasted%20image%2020230306145416.png)
- ![](../images/Pasted%20image%2020230306145426.png)



