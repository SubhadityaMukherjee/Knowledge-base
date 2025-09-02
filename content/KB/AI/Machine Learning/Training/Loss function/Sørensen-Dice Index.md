---
toc: true
title: Sørensen-Dice Index

tags: ['loss']
date modified: Monday, October 10th 2022, 2:02:15 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# Sørensen-Dice Index
- very similar to Jaccard index
- Although they are calculated similarly the Sørensen-Dice index is a bit more intuitive because it can be seen as the percentage of overlap between two sets, which is a value between 0 and 1
- overstate the importance of sets with little to no ground truth positive sets
- As a result, it could dominate the average score taken over multiple sets
- It weights each item inversely proportionally to the size of the relevant set rather than treating them equally.
- $$D(x,y) = \frac{2|x\cap y|}{|x|+|y|}$
- ![](../images/Pasted%20image%2020220624121258.png)



