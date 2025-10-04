---
toc: true
title: Multi Teacher Distillation

tags: ['knowledgedistillation']
date modified: Monday, October 10th 2022, 2:02:09 pm
date created: Tuesday, October 4th 2022, 11:49:00 am
---

# Multi Teacher Distillation
- The multiple teacher networks can be individually and integrally used for distillation during the period of training a student network.
- To transfer knowledge from multiple teachers, the simplest way is to use the averaged response from all teachers as the supervision signal (Hinton et al., 2015)
- In addi- tion to the averaged [Logits](Logits.md) from all teachers, You et al. (2017) further incorporated features from the inter- mediate layers in order to encourage the dissimilarity among different training samples.
- Fukuda et al. (2017) randomly selected one teacher from the pool of teacher networks at each it- eration. To transfer feature-based knowledge from mul- tiple teachers, additional teacher branches are added to the student networks to mimic the intermediate features of teachers (Park and Kwak, 2020; Asif et al., 2020). Born again networks address multiple teach- ers in a step-by-step manner, i.e., the student at the t step is used as the teacher of the student at the t+1 step (Furlanelloetal., 2018)
- To effi- ciently perform knowledge transfer and explore the power of multiple teachers, several alternative meth- ods have been proposed to simulate multiple teach- ers by adding different types of noise to a given teacher (Sau and Balasubramanian, 2016) or by us- ing stochastic blocks and skip connections (Lee et al., 2019c). Using multiple teacher models with feature ensembles, knowledge amalgamation is designed in (Shen et al., 2019a; Luo et al., 2019; Shen et al., 2019b; Luo et al., 2020). Through knowledge amalgamation, many public available trained deep models as teachers can be reused.



