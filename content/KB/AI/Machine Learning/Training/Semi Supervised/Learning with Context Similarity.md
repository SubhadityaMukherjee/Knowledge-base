---
toc: true
title: Learning with Context Similarity
tags: ['semisupervisedlearning']
---

## Learning with Context Similarity
- Clustering is a method of grouping sets of similar data in the same clusters 
- powerful ability of grouping data by using the attributes of the data 
- In the self-supervised scenario, the clustering methods mainly employed as a tool to cluster image data 
- A naive method would be to cluster the image data based on the hand-designed feature such as HOG [140], SIFT [141], or Fisher Vector [49] 
- After the clustering, several clusters are obtained while the image within one cluster has a smaller distance in feature space and images from different clusters have a larger distance in feature space 
- The smaller the distance in feature space, the more similar the image in the appearance in the RGB space 
- Then a ConvNet can be trained to classify the data by using the cluster assignment as the pseudo class label 
- the ConvNet needs to learn the invariance within one class and the variance among different classes 
- Therefore, the ConvNet is able to learn semantic meaning of images 
- Firstly, the image is clustered into different clusters which the images from the same cluster have smaller distance and images from different clusters have larger distance 
- Then a ConvNet is trained to recognize the cluster assignment [34], [44] or to recognize whether two imaged are from same cluster [43] 
- DeepCluster iteratively clusters images with Kmeans and use the subsequent assignments as supervision to update the weights of the network



