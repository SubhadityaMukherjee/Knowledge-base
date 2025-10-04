---
toc: true
title: EigenCAM

tags: ['explainability']
date modified: Monday 12th June 2023, Mon
date created: Monday 12th June 2023, Mon
---

# EigenCAM

- @banymuhammadEigenCAMVisualExplanations2021

## Summary by Me
Another method for computing Saliency Maps without modifying the architecture of the network, EigenCAM was proposed by Bany et al. \cite{banymuhammadEigenCAMVisualExplanations2021}. EigenCAM uses a combination of an Eigen analysis of the class activated output by projecting it on the input, and a PCA of it to remove unnecessary features from the maps. The Eigen-Saliency map is computed across the network and produces sharper outputs based on the distance (using PCA) from the input image. EigenCAM and Eigen Saliency maps were fused by a point wise multiplication operation. 


