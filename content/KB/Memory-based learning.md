---
toc: true
title: Memory-based learning

tags: ['language']
date modified: Monday, October 10th 2022, 2:02:22 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# Memory-based Learning
- Lazy learning
- All encountered examples are stored in memory in a multi-dimensional array, positioned according to relevant [Features](Features.md)
- New items are classified (comprehension) or generated (production) by searching for an example in memory that is closest to the target
- Because examplars are represented by their [Features](Features.md) even novel forms can be classified
- A generalization of the knn (k-nearest neighbors) algorithm
- Don't remove any infrequent or even solo forms. You might need the info
- Don't trim down the number of examples of a frequent form you have in the model. This effects it.
- Learning is storing, classification is analogy
- multiple long-distance dependencies



