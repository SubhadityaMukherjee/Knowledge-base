---
toc: true
title: LDA

tags: ['temp']
date modified: Sunday 25th December 2022, Sun
date created: Sunday 25th December 2022, Sun
---

# LDA


## Steps
-   Compute the dd-dimensional mean vectors for the different classes from the dataset.
-   Compute the scatter matrices (in-between-class and within-class scatter matrix).
-   Compute the eigenvectors $(e_1,e_2,...,e_de_1,e_2,...,e_d)$ and corresponding eigenvalues $(λ_1,λ_2,...,λ_dλ_1,λ_2,...,λ_d)$ for the scatter matrices.
-  Sort the eigenvectors by decreasing eigenvalues and choose $k$ eigenvectors with the largest eigenvalues to form a $d×k$ dimensional matrix $W$ (where every column represents an [Eigenvector](Eigenvector.md)).
-  Use this $d×k$ [Eigenvector](Eigenvector.md) matrix to transform the samples onto the new subspace. This can be summarized by the matrix multiplication: $Y=X×WY=X×W$ (where $X$ is a $n×d$-dimensional matrix representing the $n$ samples, and $y$ are the transformed $n×k$-dimensional samples in the new subspace).



