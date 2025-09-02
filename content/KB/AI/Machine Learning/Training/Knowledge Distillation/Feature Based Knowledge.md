---
toc: true
title: Feature Based Knowledge

tags: ['knowledgedistillation']
date modified: Monday, October 10th 2022, 2:02:09 pm
date created: Tuesday, October 4th 2022, 11:44:14 am
---

# Feature Based Knowledge
- Huang and Wang (2017) using neuron selectivity trans- fer. Passalis and Tefas (2018) transferred knowledge by matching the probability distribution in feature space.
- Kim et al. (2018) introduced so called “factors” as a more understandable form of intermediate repre- sentations. To reduce the performance gap between teacher and student, Jin et al. (2019) proposed route constrained hint learning, which supervises student by outputs of hint layers of teacher. Recently, Heo et al. (2019c) proposed to use the activation boundary of the hidden neurons for knowledge transfer. Interestingly, the parameter sharing of intermediate layers of the teacher model together with response-based knowledge is also used as the teacher knowledge (Zhou et al., 2018).
- To match the semantics between teacher and stu- dent, Chen et al. (2021) proposed cross-layer knowledge distillation, which adaptively assigns proper teacher layers for each student layer via [Attention](Attention.md) allocation.
- Though feature-based knowledge transfer provides favorable information for the learning of the student model, how to effectively choose the hint layers from the teacher model and the guided layers from the student model remains to be further investigated (Romero et al., 2015).
- [Distillation Schemes](Distillation%20Schemes.md)
- [Teacher Student Architecture](Teacher%20Student%20Architecture.md)
- [Distillation Algorithms](Distillation%20Algorithms.md)
- [Applications of Knowledge Distillation](Applications%20of%20Knowledge%20Distillation.md)
- For example, on one hand, some recent works find that the student model can learn little from some teacher models due to the model capac- ity gap between the teacher model and the student model (Zhang et al., 2019b; Kang et al., 2020); On the other hand, from some early theoretical analysis on the capacity of neural networks, shallow networks are capable of learning the same representation as deep neural networks (Ba and Caruana, 2014).



