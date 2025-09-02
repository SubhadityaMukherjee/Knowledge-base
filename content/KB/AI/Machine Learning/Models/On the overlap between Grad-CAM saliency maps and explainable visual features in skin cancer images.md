---
toc: true
title: On the overlap between Grad-CAM saliency maps and explainable visual features in skin cancer images

tags: ['explainability']
date modified: Tuesday, January 24th 2023, 8:22:29 pm
date created: Thursday, October 6th 2022, 10:29:54 am
---

# On the Overlap Between [Grad-CAM](Grad-CAM.md) Saliency Maps and Explainable Visual Features in Skin Cancer Images
- @nunnariOverlapGradCAMSaliency2021
- Nunnari, Fabrizio, Md Abdul Kadir, and Daniel Sonntag. 2021. “On the Overlap Between [Grad-CAM](Grad-CAM.md) Saliency Maps and Explainable Visual Features in Skin Cancer Images.” Pp. 241–53 in _Machine Learning and Knowledge Extraction_. Vol. 12844, _Lecture Notes in Computer Science_, edited by A. Holzinger, P. Kieseberg, A. M. Tjoa, and E. Weippl. Cham: Springer International Publishing.

## Intro
- Dermatologists recognize melanomas by inspecting images in which they identify human-comprehensible visual features.
- investigate to what extent such features correspond to the saliency areas identified on CNNs trained for classification
- Saliency maps are images that indicate the pixels areas contributing to a certain classification decision. Saliency maps are normally encoded as greyscale images or converted to heatmaps for visual inspection.
- to what extent saliency maps can be used to identify visual features of skin lesions

## Related Work
- [ISIC 2018](ISIC%202018.md)
- [RISE](RISE.md)
- Jahanifar et al. also propose a modified DRFI (Discriminative Regional Feature Integration) technique for a similar task for multi-level segmentation task
- By combining multiple segmentation masks, they produce a more accurate mask.
- During the generation of the mask, they use a threshold value of 0.5, but they did not provide a reason for which they choose this value.

## Classification Architectures and Models
- RESNET50
- VGG16

## Data Preparation
- As an additional feature, we compute the pixels-wise union of all the features
- In our experiments, we ignore the skin lesion samples with no features.
- The generation of the saliency maps consists of running the [Grad-CAM](Grad-CAM.md) algorithm on each skin lesion picture with non-black union mask
- We repeat the procedure for both the VGG16 and the RESNET50 models, generating the SV and SR greyscale picture sets
- To compare the saliency maps with ground truth maps, we scaled up SV and SR to the resolution of the original images using a nearest neighbour filter.
- We can observe that all distributions are strongly right skewed, and all $J_{s}$ are mostly below 0.2, with the exception of a peak in performance for the pigment network clas

## First Experiment
- With the first experiment we aim at identifying the threshold value that leads to a maximization of the overlap between saliency maps and ground truth
- To do so, we converted each saliency map into 11 binary maps using thresholds from 0.0 to 1.0 with steps of 0.1
- Then, we proceed by computing the Jaccard indices J between the ground truth and all of the processed saliencies S x V and S x R.
- For VGG16, among the features classes, the best threshold ranges between 0.4 and 0.7. The minimum J index is 0.0 on all categories, meaning that among all samples there is always at least one map with zero-overlap with the ground truth. The highest average (J=0.141) and maximum (J=0.797) belong to the pigmented network class.
- When switching to RESNET50, the best thresholds range between 0.3 and 0.7. With respect to VGG16, pigmented network and streaks present the worse performance, while the average J increases for the other three classes
- Surprisingly, the Jaccard indices measured with the RESNET50 maps, which have a resolution limited to 8x8 pixels, are comparable to the ones extracted from the VGG16 models (24x24 pixels)
- The second hypothesis is that the lower resolution of the RESNET50 maps is compensated by the higher accuracy of the classification model, i.e., a better overall overlap.

## Second Experiment
- diving the samples into Melanoma and Nevus, and into correctly vs. wrongly classified samples.
- Here, the Jaccard indices are calculated using the union feature and using the best threshold identified in the first experiment, hence on S 0.5 R V and S 0.3
- For VGG16, we can observe that the mean J for correctly classified melanomas (0.135) is similar to the union class average (0.132).
- However, when melanomas are wrongly classified, the Jaccard index drops to 0.086, meaning that the saliency maps diverges from the ground truth

## Observation
- This could effectively help doctors is spotting a wrong classification
- The idea is that: if the classifier tells the doctor that the sample is a melanoma, but then the reported saliency areas diverge a lot from what would be manually marked, then doctors can be more easily induced to think that the system is misclassifying the image

## Discussion
- Among the five features, only Pigment Network reaches the same level of accuracy of the union class.
- maximum J=0.136
- This is a huge annotation overhead when compared to labeling images with their diagnose class.
- The value of the threshold to reach the best J index varies among datasets and features. Since it is not possible to analytically foresee the best threshold of a given dataset, we suggest the development of interactive exploratory visual interfaces, where dermatologists can autonomously control the saliency threshold value in an interactive fashion for exploration.
- However, from a decomposition between classes and correctness of classification, it appears that, for higher resolution maps (24x24 pixels on VGG16), saliency maps overlap much better with ground truth features when the classifier is correctly classifying a melanoma (J=0.135) and performance drops when the prediction is incorrect (J=0.086).
- Further, we would like to investigate on better options for thresholding. In this paper, a global threshold, in the range of 0.0 to 1.0, was simultaneously searched and applied to all the saliency map.
- This allows for an "emersion" of the most relevant region of interests of a global scale
- However, there might be regions of saliency below the global threshold which are relevant with respect to the local surrounding area
- To spot local maxima, we could split the maps into tiles, or super-pixels, and iteratively identify multiple local threshold values based on the range of saliency values of each region.
- Finally, the current implementation of [Grad-CAM](Grad-CAM.md) returns saliency maps whose range is filled by stretching the range of activation values of the target convolution layer.
- Each saliency map is forced to use the full activation range, independent of other samples.
- In so doing, regions of interests are "forced" to emerge, even when the activation values of the inner layer are lower when compared to other images.

## Future Work
- As future work, we could consider performing saliency normalization according to global statistics (mean and variance) on the tested set.

## Images
- ![](../images/Pasted%20image%2020221006103042.png)



