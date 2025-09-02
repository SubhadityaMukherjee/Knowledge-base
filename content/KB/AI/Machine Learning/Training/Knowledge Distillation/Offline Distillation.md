---
toc: true
title: Offline Distillation

tags: ['knowledgedistillation']
date modified: Monday, October 10th 2022, 2:02:09 pm
date created: Tuesday, October 4th 2022, 11:45:59 am
---

# Offline Distillation
- The first stage in offline distillation is usually not discussed as part of knowledge distillation, i.e., it is assumed that the teacher model is pre-defined. Little at- tention is paid to the teacher model structure and its re- lationship with the student model
- The main advantage of offline methods is that they are simple and easy to be implemented. For example, the teacher model may contain a set of mod- els trained using different software packages, possibly located on different machines. The knowledge can be extracted and stored in a cache.
- The offline distillation methods usually employ one- way knowledge transfer and two-phase training pro- cedure. However, the complex high-capacity teacher model with huge training time can not be avoided, while the training of the student model in offline distillation is usually efficient under the guidance of the teacher model.
- Moreover, the capacity gap between large teacher and small student always exists, and student often largely relies on teacher.



