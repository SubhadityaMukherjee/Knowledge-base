---
tags: ['temp']
toc: true
title: Sketched Update
date modified: Monday, October 10th 2022, 2:02:16 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# Sketched Update
- Learn a full model update, then compress it before sending to the server.
- First computes the full Hit during local training without any constraints, and then approximates, or encodes, the update in a (lossy) compressed form before sending to the server. The server decodes the updates before doing the aggregation.
- Subsampling - Instead of sending Hit , each client only communicates matrix Ĥit which is formed from a random subset of the (scaled) values of Hit.
- Quantize the weights -Improving the quantization by structured random rotations. The above 1-bit and multi-bit quantization approach work best when the scales are approximately equal across different dimensions.
- In the decoding phase, the server needs to perform the inverse rotation before aggregating all the updates.



