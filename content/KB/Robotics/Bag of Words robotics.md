---
toc: true
title: Bag of Words Robotics
tags: ['robotics']
date created: Friday, November 25th 2022, 12:05:56 pm
date modified: Wednesday, December 7th 2022, 10:37:52 pm
---


# Bag of Words Robotics
- Recognizing objects using local descriptors would be computationally expensive.
- The number of local features for a given object mainly depends on the size of the object, and therefore, varies for different objects.
- The key idea for fast 3D object recognition is to use mechanisms for representing objects in a compact and uniform format (e.g., histogram).
- If we represent objects in a uniform format, then we can apply ML algorithms
- Compute local features for all the discovered objects and make a pool of features.
- A dictionary is generated via [[Clustering]] of the pool of features into N clusters (the number of the clusters is the codebook size).
- Visual word are then defined as the centres of the extracted clusters.
- Finally, each object is described (abstracted) by a histogram of occurrences of these visual words.
- ![[Pasted image 20221103123459.webp]]
- ![[Pasted image 20221103123515.webp]]



