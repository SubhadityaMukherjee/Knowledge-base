---
toc: true
title: Jaccard Distance

tags: ['loss']
date modified: Monday, October 10th 2022, 2:02:24 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# Jaccard Distance
- $$D(x,y) = 1- \frac{x\cup y}{x\cap y}$$
- The Jaccard index (or Intersection over Union) is a metric used to calculate the similarity and diversity of sample sets. It is the size of the intersection divided by the size of the union of the sample sets.
- In practice, it is the total number of similar entities between sets divided by the total number of entities.
- To calculate the Jaccard distance we simply subtract the Jaccard index from 1
- highly influenced by the size of the dat
- Large datasets can have a big impact on the index as it could significantly increase the union whilst keeping the intersection similar
- The Jaccard index is often used in applications where binary or binarized data are used
- deep learning model predicting segments of an image
- text similarity analysis to measure how much word choice overlap there is between documents



