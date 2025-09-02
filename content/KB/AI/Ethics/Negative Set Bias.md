---
toc: true
title: Negative Set Bias

tags: ['ethics']
date modified: Wednesday, January 25th 2023, 11:54:55 am
date created: Wednesday, January 25th 2023, 11:54:54 am
---

# Negative Set Bias


- Datasets define a visual phenomenon (e.g. object, scene, event) not just by what it is (positive instances), but also by what it is not (negative instances)
- the space of all possible negatives in the visual world is astronomically large, so datasets are forced to rely on only a small sample
- ImageNet benefits from a large variability of negative examples and does not seem to be affected by a new external negative set, whereas Caltech and MSRC appear to be just too easy
- Unfortunately, it's not at all easy to stress-test the sufficiency of a negative set in the general case since it will require huge amounts of labelled (and unbiased) negative data.
- One remedy, proposed in this paper, is to add negatives from other datasets
- Another approach, suggested by Mark Everingham, is to use a few standard algorithms (e.g. bag of words) to actively mine hard negatives as part of dataset construction from a very large unlabelled set, and then manually going through them to weed out true positives. The down side is that the resulting dataset will be biased against existing algorithms.



