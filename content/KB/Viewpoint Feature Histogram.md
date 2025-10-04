---
toc: true
title: Viewpoint Feature Histogram
tags: ['robotics']
---

# Viewpoint Feature Histogram
- VFH produces a histogram that encodes the geometry of the object and its viewpoint.
- For every pair of a point and the center of mass, a reference frame is constructed and the three angular variations are computed (a, q, f) and also d which represents distance between (point, center of mass)
- Another statistical feature is computed between the central viewpoint direction and the normal estimated at each point.
- The quality of VFH description depends on the quality of the surface normal estimation at each point.
- ![](../images/Pasted%20image%2020221103123406.png)



