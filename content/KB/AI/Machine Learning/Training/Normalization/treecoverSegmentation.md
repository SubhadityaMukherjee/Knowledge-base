---
toc: true
title: Tree Cover Segmentation
tags: ['application']
date modified: Monday, October 10th 2022, 2:02:09 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# Tree Cover Segmentation
- treecover segmentation [PointNet++](PointNet++.md)
	- Data collected from above
	- Normalization : height, xy
	- Rotation
	- Jiggling ??
	- Labeling
		- ![](../images/Pasted%20image%2020220318094643.png) Segmentation algorithm. Canopy hide model
		- Weighted [loss](../Tag%20Pages/loss.md) + [Focal Loss](Focal%20Loss.md)

## 2d Methods
- [Watershed](Watershed) + [Unet](Unet.md)
- ![](../images/Pasted%20image%2020220318100323.png)
- ![](../images/Pasted%20image%2020220318100634.png)
	- $\Theta$ is just clippingpng]
	- The sqrt makes it a little smoother

## Ref
- Max Freudenberg - Gottingen Uni Germany
- Adrian Stroker - Gottingen Uni Germany



