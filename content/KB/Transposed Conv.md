---
toc: true
title: Transposed Conv

tags: ['architecture']
date modified: Saturday, December 17th 2022, 1:47:49 pm
date created: Thursday, December 15th 2022, 10:05:01 pm
---

# Transposed Conv

- use a transformation going in the opposite direction of a normal convolution, i.e., from something that has the shape of the output of some convolution to something that has the shape of its input while maintaining a connectivity pattern that is compatible with said convolution.
- Upsampling
- Input i, kernel k, padding p, stride s , $$o = (i-1) \times s +k -2p$$
- Steps
	- Calculate new Param's z and p'
	- Between each row and columns of the input, insert z number of zeros. This increases the size of the input to $(2*i -1) \times (2*i -1)$
	- Pad the modified image with p' no of zeros
	- Standard conv with stride of 1
	- ![3BEF01EA-1132-4BBA-965F-4C4D75BDD9BA.webp](3BEF01EA-1132-4BBA-965F-4C4D75BDD9BA.webp.md)
- ![](../images/031324A4-A9BA-4615-A81D-82BC53564751.png)



