---
toc: true
title: Applications of Knowledge Distillation

tags: ['knowledgedistillation']
date modified: Monday, October 10th 2022, 2:02:09 pm
date created: Tuesday, October 4th 2022, 11:53:11 am
---

# Applications of Knowledge Distillation
- Specifically, in (Luo et al., 2016), the knowledge from the chosen informative neurons of top hint layer of the teacher network is trans- ferred into the student network
- A recursive knowledge distillation method was designed by using a previous student network to ini- tialize the next one (Yan et al., 2019). Since most face recognition methods perform the open-set recognition, i.e., the classes/identities on test set are unknown to the training set, the face recognition criteria are usually distance metrics between feature representations of positive and negtive samples, e.g., the angular loss in (Duong et al., 2019) and the correlated embedding loss in (Wu et al., 2020).
- Specifically, Ge et al. (2018) proposed a selective knowledge distillation method, in which the teacher network for high-resolution face recognition selectively transfers its informative facial features into the student network for low-resolution face recognition through sparse graph optimization. In (Kong et al., 2019), cross- resolution face recognition was realized by designing a resolution invariant model unifying both face halluci- nation and heterogeneous recognition sub-nets. To get efficient and effective low resolution face recognition model, the multi-kernel maximum mean discrepancy between student and teacher networks was adopted as the feature loss (Wang et al., 2019c).
- KD-based face recognition can be extended to face alignment and verification by changing the losses in knowledge distillation (Wang et al., 2017).
- For incomplete, ambiguous and redundant image labels, the label refinery model through self-distillation and label progression is proposed to learn soft, informative, collective and dynamic labels for complex image classi- fication (Bagherinezhad et al., 2018).
- To address catas- trophic forgetting with CNN in a variety of image clas- sification tasks, a learning without forgetting method for CNN, including both knowledge distillation and lifelong learning is proposed to recognize a new image task and to preserve the original tasks (Li and Hoiem, 2017).
- For improving image classification accuracy, Chen et al. (2018a) proposed the feature maps-based knowledge distillation method with GAN.
- Similar to the KD-based low-resolution face recognition, Zhu et al. (2019) proposed deep feature distillation for the low-resolution image classification, in which the output features of a student match that of teacher.
- Gordon and Duh (2019) explained the good perfor- mance of sequence-level knowledge distillation from the perspective of data augmentation and regulariza- tion. In (Kim and Rush, 2016), the effective word-level knowledge distillation is extended to the sequence- level one in the sequence generation scenario of NMT. The sequence generation student model mimics the sequence distribution of the teacher. To overcome the multilingual diversity, Tan et al. (2019) proposed multi teacher distillation, in which multiple individual models for handling bilingual pairs are teacher and a mul- tilingual model is student.
- To improve the transla- tion quality, an ensemble of mutiple NMT models as teacher supervise the student model with a data filtering method Freitag et al. (2017).
- (Wei et al., 2019) proposed a novel online knowledge distillation method, which addresses the unstableness of the training process and the decreasing performance on each validation set.
- The proposed pre- trained distillation performs well in sentiment classifi- cation, natural language inference, textual entailment. For a multi-task distillation in the context of natu- ral language understanding, Clark et al. (2019) pro- posed the single-multi born-again distillation, which is based on born-again neural networks (Furlanello et al., 2018).
- In (Perez et al., 2020), a audio-visual multi- modal knowledge distillation method is proposed. knowl- edge is transferred from the teacher models on visual and acoustic data into a student model on audio data.
- Pan et al. (2019) designed a enhanced collaborative [Denoising Autoencoder](Denoising%20Autoencoder.md) (ECAE) model for recommender systems via knowledge distillation to capture useful knowledge from user feedbacks and to reduce noise. The unified ECAE framework contains a generation network, a retraining network and a distillation layer that trans- fers knowledge and reduces noise from the generation network.



