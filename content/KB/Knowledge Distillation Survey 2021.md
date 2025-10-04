---
toc: true
title: Knowledge Distillation Survey 2021

tags: ['knowledgedistillation']
date modified: Monday, October 10th 2022, 2:02:09 pm
date created: Tuesday, October 4th 2022, 11:40:36 am
---

# Knowledge Distillation Survey 2021
- model compression and acceleration techniques
- [Low-rank factorization](Low-rank%20factorization.md)
- [Transferred compact convolutional filters](Transferred%20compact%20convolutional%20filters.md)
- To address this issue, Bucilua et al. (2006) first proposed model compression to transfer the information from a large model or an ensem- ble of models into training a small model without a significant drop in accuracy. The knowledge transfer between a fully-supervised teacher model and a stu- dent model using the unlabeled data is also intro- duced for semi-supervised learning (Urner et al., 2011).
- The learning of a small model from a large model is later formally popularized as knowledge distilla- tion (Hinton et al., 2015). In knowledge distillation, a small student model is generally supervised by a large teacher model (Bucilua et al., 2006; Ba and Caruana, 2014; Hinton et al., 2015; Urban et al., 2017).
- The main idea is that the student model mimics the teacher model in order to obtain a competitive or even a superior performance. The key problem is how to transfer the knowledge from a large teacher model to a small student model. Basically, a knowledge distillation system is composed of three key components: knowledge, dis- tillation algorithm, and teacher-student architecture.
- Successful distillation relies on data geometry, optimization bias of distillation objective and strong monotonicity of the student classifier
- quantified the extraction of visual concepts from the intermediate layers of a deep neural network, to explain knowledge distillation (Cheng et al., 2020). Ji & Zhu theoretically explained knowledge distillation on a wide neural network from the respective of risk bound, data efficiency and imperfect teacher (Ji and Zhu., 2020).
- Knowledge distillation has also been explored for [Label Smoothing](Label%20Smoothing.md), for assessing the accuracy of the teacher and for obtaining a prior for the optimal output layer geometry (Tang et al., 2020).
- Furthermore, the knowledge transfer from one model to another in knowledge distillation can be extended to other tasks, such as adversar- ial attacks (Papernot et al., 2016), data augmenta- tion (Lee et al., 2019a; Gordon and Duh, 2019), data privacy and security (Wang et al., 2019a).
- A vanilla knowledge distillation uses the [Logits](Logits.md) of a large deep model as the teacher knowledge (Hinton et al., 2015; Kim et al., 2018; Ba and Caruana, 2014; Mirzadeh et al., 2020)
- Further- more, the parameters of the teacher model (or the connections between layers) also contain another knowl- edge (Liu et al., 2019c)
- [Response Based Knowledge](Response%20Based%20Knowledge.md)
- [Feature Based Knowledge](Feature%20Based%20Knowledge.md)



