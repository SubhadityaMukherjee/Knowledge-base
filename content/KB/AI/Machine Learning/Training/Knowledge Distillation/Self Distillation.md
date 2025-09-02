---
toc: true
title: Self Distillation

tags: ['knowledgedistillation']
date modified: Monday, October 10th 2022, 2:02:09 pm
date created: Tuesday, October 4th 2022, 11:46:29 am
---

# Self Distillation
- To be specific, Yuan et al. proposed teacher-free knowledge distillation meth- ods based on the analysis of [Label Smoothing](Label%20Smoothing.md) reg- ularization (Yuan et al., 2020). Hahn and Choi pro- posed a novel self-knowledge distillation method, in which the self-knowledge consists of the predicted probabilities instead of traditional soft probabilities (Hahn and Choi, 2019).
- These predicted probabilities are defined by the feature representations of the train- ing model. They reflect the similarities of data in feature embedding space. Yun et al. proposed class- wise self-knowledge distillation to match the output distributions of the training model between intra- class samples and augmented samples within the same source with the same model (Yun et al., 2020).
- In addition, the self-distillation proposed by Lee et al. (2019a) is adopted for data augmentation and the self- knowledge of augmentation is distilled into the model itself. Self distillation is also adopted to optimize deep models (the teacher or student networks) with the same architecture one by one (Furlanello et al., 2018; Bagherinezhad et al., 2018)
- both self-distillation and online distillation are properly in- tegrated via the multiple knowledge transfer frame- work (Sun et al., 2021).



