---
toc: true
title: SLAK

tags: ['architecture']
date modified: Sunday, October 23rd 2022, 5:04:23 pm
date created: Sunday, October 23rd 2022, 4:56:57 pm
---

# SLAK
- MORE CONVNETS IN THE 2020S: SCALING UP KERNELS BEYOND 51 × 51 USING [Sparsity](Sparsity.md)
- Shiwei Liu, Tianlong Chen, Xiaohan Chen, Xuxi Chen, Qiao Xiao, Boqian Wu, Tommi Ka ̈ rkka ̈ inen, Mykola Pechenizkiy, Decebal Constantin Mocanu, Zhangyang Wang


- The dominant role of convolutional neural networks (CNNs) seems to be challenged by increasingly effective transformer-based models.
- advanced convolutional models strike back with large ker- nels motivated by the local-window attention mechanism, showing appealing perfor- mance and efficiency
- [RepLKNet](RepLKNet.md)
- This study ends up with a recipe for applying extremely large kernels from the perspective of [Sparsity](Sparsity.md), which can smoothly scale up kernels to 61×61 with better performance
- Built on this recipe, we propose Sparse Large Kernel Network (SLaK), a pure CNN architec- ture equipped with sparse factorized 51×51 kernels that can perform on par with or better than state-of-the-art hierarchical Transformers and modern ConvNet architec- tures like ConvNeXt and RepLKNet

## RELATED WORK
- [Large Kernel in Attention](Large%20Kernel%20in%20Attention.md)
- [Large Kernel in Convolution](Large%20Kernel%20in%20Convolution.md)
- [Dynamic Sparsity](Dynamic%20Sparsity.md)
- [Sparse Evolutionary Training](Sparse%20Evolutionary%20Training.md)

## FAILURES OF EXISTING APPROACHES TO GO BEYOND 31x31 KERNELS
- It is important to note that all models are trained for a reduced length of 120 epochs in this section, just to sketch the scaling trends of large kernel sizes.
- Following the design in RepLKNet, we set the kernel size of each stage as [51, 49, 47, 13] and [61, 59, 57, 13],
- naively enlarging kernel size from 7x7 to 31x31 decreases the performance although the receptive field may be enlarged by using extremely large kernels, it
- might fail to maintain the desirable property of locality.
- Since the stem cell in standard ResNet (He et al., 2016) and ConvNeXt results in a
- 4x [Downsampling](Downsampling.md) of the input images, extreme kernels with

## A RECIPE FOR EXTREMELY LARGE KERNELS BEYOND 31x31
- Decomposing a large kernel into two rectangular, parallel kernels smoothly scales the kernel size up to 61x61
- Although using convolutions with medium sizes (e.g., 31x31) seemingly can directly avoid this problem, we want to investigate if we can further push the performance of CNNs by using (global) extreme convolutions
- approximate the large MxM kernel with a combination of two parallel and rectangular convolutions whose kernel size is MxN and NxM (where N < M), respectively, as shown in Figure 1. Following Ding et al. (2022), we keep a 5x5 layer parallel to the large kernels and summed up their outputs after a batch norm layer.
- This decomposition balances between capturing long-range dependencies and extracting local detail features
- In stark contrast, the overhead of our method increases just linearly with the kernel size
- As the decomposition reduces learnable parameters and FLOPs, it is no surprise to observe our network to initially sacrifice accuracy slightly compared to the original RepLKNet at medium kernel sizes i.e. 31x31
- However, as the convolution size continues to increase, our method can scale kernel size up to 61x61 with improved performance.

### Use Sparse Groups, Expand More Width
- significantly boosts the model capacity.
- Instead of using the standard group convolution, ConvNeXt simply employs depthwise convolutions with an increased width to achieve the goal of "use more groups, expand width". In this paper, we attempt to extend this principle from a [Sparsity](Sparsity.md)-inspired perspective – "use sparse groups, expand more width".
- replace the dense convolutions with sparse convolutions, where the sparse kernels are randomly constructed based on the layer-wise [Sparsity](Sparsity.md) ratio of SNIP (Lee et al., 2019)
- After construction, we train the sparse model with dynamic [Sparsity](Sparsity.md) (Mocanu et al., 2018; Liu et al., 2021b), where the sparse weights are dynamically adapted during training by pruning the weights with the lowest magnitude and growing the same number of weights randomly.
- Doing so enables dynamic adaptation of sparse weights, leading to better local features.
- As kernels are sparse throughout training, the corresponding parameter count and training/inference FLOPs are only proportional to the dense models.
- dynamic [Sparsity](Sparsity.md) notably reduces more than 2.0 GFLOPs, despite causing temporary performance degradation.
- Dynamic [Sparsity](Sparsity.md) allows us to computation-friendly scale the model size up
- For example, using the same [Sparsity](Sparsity.md) (40%), we can expand the model width by 1.3x while keeping the parameter count and FLOPs roughly the same as the dense model

### Large Kernels Generalize Better Than Small Kernels with Our Recipe
- performance consistently increases with kernel size, up to 51x51
- Applying each part of our proposed recipe to 7x7 kernels leads to either no gain or marginal gains compared to our 51x51 kernels. This break-down experiment justifies our claim: large kernel is the root of power, and our proposed recipe helps unleash such power from large kernels.

## SLAK
- SLaK is built based on the architecture of ConvNeXt
- The design of the stage compute ratio and the stem cell are inherited from ConvNeXt
- The number of blocks in each stage is [3, 3, 9, 3] for SLaK-T and [3, 3, 27, 3] for SLaK-S/B
- The stem cell is simply a convolution layer with 4x4 kernels and 4 strides. Page 6
- We first directly increase the kernel size of ConvNeXt to [51, 49, 47, 13] for each stage, and replace each MxM kernel with a combination of Mx5 and 5xM kernels
- We find that adding a BatchNorm layer directly after each decomposed kernel is crucial before summing the output up
- urther sparsify the whole network and expand the width of stages by 1.3x, ending up with SLaK

## EVALUATION OF SLAK ImageNet-1K
- ADE20K
- PASCAL VOC 2007
- COCO
- SLaK is not only able to capture long-range dependence but also the local context features.
- In comparison, high-contribution pixels of SLaK spread in a much larger ERF, and some high-contribution pixels emerge in non-center areas.
- SLaK balances between capturing long-range dependencies and focusing on the local details.
- SLaK seems to automatically recover the inductive bias of peripheral vision (Lettvin et al., 1976; Min et al., 2022) in the human vision system: the entire visual field is partitioned into multiple regions from near the gaze center to distant areas; humans have high- resolution processing near the gaze center (central and para-central regions), and decrease the resolution of processing for mid and far peripheral regions.

### KERNEL SCALING EFFICIENCY
- We simply replace all the kernels in stages of ConvNeXt-T with a set of kernel sizes from 7 to 151 and report the required GFLOPs and the number of parameters
- One can clearly see the big gap between full-kernel scaling (yellow lines) and kernel decomposition (green lines) as the kernel size increases beyond 31x31.
- Even using the ultra-large 151x151 kernels, using our methods would require fewer FLOPs and parameters, compared to full-kernel scaling with 51x51 kernel
- EFFECTIVE RECEPTIVE FIELD (ERF)

## Experiment

### SETTINGS IMAGENET-1K
- We share the (pre-)training settings of SLaK on ImageNet-1K in this section. We train SLaK for 300 epochs (Section 5.1) and 120 epochs (Section 4) using AdamW (Loshchilov & Hutter, 2019) with a batch size of 4096, and a weight decay of 0.05. The only differnce between models training for 300 epochs and 120 epochs is the training time. The learning rate is 4e-3 with a 20-epoch linear warmup followed by a cosine decaying schedule. For data augmentation, we use the default setting of [RandAugment] (Cubuk et al., 2020) in Timm (Wightman, 2019) – "rand-m9-mstd0.5- inc1", Label Smoothing (Szegedy et al., 2016) coefficient of 0.1, Mixup (Zhang et al., 2017) with ↵ = 0.8, [Cutmix] (Yun et al., 2019) with ↵ = 1.0, [Random Erasing](RandAugment] (Cubuk et al., 2020) in Timm (Wightman, 2019) – "rand-m9-mstd0.5- inc1", Label Smoothing (Szegedy et al., 2016) coefficient of 0.1, Mixup (Zhang et al., 2017) with ↵ = 0.8, [Cutmix] (Yun et al., 2019) with ↵ = 1.0, [Random Erasing.md) (Zhong et al., 2020) with p = 0.25, Stochastic Depth with drop rate of 0.1 for SLaK-T, 0.4 for SLaK-S, and 0.5 for SLaK-B, Layer Scale (Touvron et al., 2021c) of initial value of 1e- 6, and EMA with a decay factor of 0.9999. We train SLaK-T with NVIDIA A100 GPUs and the rest of models are trained with NVIDIA V100.

### SEMANTIC SEGMENTATION ON ADE20K
- We follow the training setting used in Ding et al. (2022); Liu et al. (2022b) using UperNet (Xiao et al., 2018) implemented by MMSegmentation (Contributors, 2020) with the 80K/160K-iteration training schedule. We conduct experiments with both short and long training procedures. The backbones are pre-trained on ImageNet-1K with 224x224 input for 120/300 epochs and then are finetuned with UperNet (Xiao et al., 2018) for 80K/160K iterations, respectively. We report the mean Intersection over Union (mIoU) with single-scale. All the hyperparameters are the exactly the same as the ones used in the official GitHub repository of ConvNeXt (con, 2021).

### OBJECT DETECTION AND SEGMENTATION ON COCO
- For COCO experiments, we follow the training settings used in BEiT, Swin, and ConvNeXt using MMDetection (Chen et al., 2019) and MMSegmentation (Contributors, 2020) toolboxes. The final model weights are adopted (instead of EMA weights) from ImageNet-1K pre-training with 224x224 input. We also conduct experiments with both short and long training procedures. The backbones are pre- trained on ImageNet-1K with 224x224 input for 120/300 epochs and then are finetuned with Cascade Mask R-CNN (Cai & Vasconcelos, 2018) for 12/36 epochs, respectively. All the hyperparameters are the exactly the same as the ones used in the official GitHub repository of ConvNeXt (con, 2021).

### OBJECT DETECTION ON PASCAL VOC 2007
- We follow (Liu et al., 2021e) and finetune Faster-RCNN on PASCAL VOC dataset with SLaK-T as the backbone. We use multi-scale setting (Carion et al., 2020; Sun et al., 2021) which leads to the length of the shorter side between 480 and 800 and the ones of the longer side at most 1333. The model is trained with AdamW for 36 epochs with a learning rate of 0.0001, a weight decay of 0.05, and a batch size of 16.

## Some More Effects

### TRADE-OFF BETWEEN [Sparsity](Sparsity.md) AND WIDTH
- As we expected, the model's performance keeps increasing as model width
- increases until the width factor reaches 1.5x, after which increasing width further starts to hurt the performance apparently due to the training difficulties associated with highly sparse neural networks.

### EFFECT OF THE SHORTER EDGE N ON SLAK
- We vary the shorter edge N 2 [3, 5, 7] and report the accuracy. All models were trained with AdamW on ImageNet-1K for 120 epochs. We empirically find that N=5 give us the best results, whereas N = 3 and N = 7 has slightly lower accuracy. We hence think it reasonable to choose N = 5 as the default option.

### ERF QUANTITATION OF MODELS WITH DIFFERENT KERNEL SIZES
- Larger r suggests a smoother distribution of high-contribution pixels. We can see that with global kernels, SLaK naturally considers a larger range of pixels to make decisions than ConvNeXt and RepLKNet.

### CONFIGURATIONS OF DYNAMIC [Sparsity](Sparsity.md)
- Following Liu et al. (2021c), we specifically tune two factors for SLaK-T that control the strength of weight adaptation, adaptation frequency f and adaptation rate p. Adaptation frequency determines after how many training iterations we adjust the sparse weights, and the latter controls the ratio of the weight that we adjust at each adaptation
- f = 2000
- and p = 0.5 works best for SLak-T. For SLak-S/B, we directly choose f = 100 and p = 0.3 without careful tuning.

## LIMITATIONS
- sparse architecture is implemented with binary masks due to the limited support of sparse neural networks by the commonly used hardware such as GPU and TPU
- Therefore, the inference FLOPs reported in the main paper are the theoretical values.
- Once this great potential is supported in the future, it can have a significant positive impact on our planet by saving a huge amount of energy and reducing overall total carbon emissions.
- Although not the focus of this current work, it would be interesting for future work to examine the speedup of sparse large kernels, using such specialized hardware accelerators, as we see much improvement room of promise here.



