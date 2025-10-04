---
toc: true
title: Graph Based Distillation

tags: ['knowledgedistillation']
date modified: Monday, October 10th 2022, 2:02:09 pm
date created: Tuesday, October 4th 2022, 11:50:22 am
---

# Graph Based Distillation
- Lee and Song (2019) analysed intra-data rela- tions using a multi-head graph, in which the vertices are the features from different layers in CNNs. Park et al. (2019) directly transferred the mutual relations of data samples, i.e., to match edges between a teacher graph and a student graph. Tung and Mori (2019) used the similarity matrix to represent the mutual relations of the activations of the input pairs in teacher and student models. The similarity matrix of student matches that of teacher.
- Peng et al. (2019a) not only matched the response-based and feature-based knowl- edge, but also used the graph-based knowledge. In (Liu et al., 2019g), the instance features and instance relationships are modeled as vertexes and edges of the graph, respectively.
- Specifically, Luo et al. (2018) considered the modal- ity discrepancy to incorporate privileged information from the source domain. A directed graph, referred to as a distillation graph is introduced to explore the relationship between different modalities. Each vertex represent a [modality] and the edges indicate the connection strength between one [modality](modality] and the edges indicate the connection strength between one [modality.md) and another.
- Minami et al. (2019) proposed a bidirectional graph-based diverse collaborative learning to explore diverse knowledge transfer patterns. Yao et al. (2020) introduced GNNs to deal with the knowledge trans- fer for graph-based knowledge.
- Besides, using knowl- edge distillation, the topological semantics of a graph convolutional teacher network as the topology-aware knowledge are transferred into the graph convolutional student network (Yang et al., 2020b)



