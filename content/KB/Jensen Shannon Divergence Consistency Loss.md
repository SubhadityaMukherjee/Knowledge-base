---
toc: true
title: Jensen Shannon Divergence Consistency Loss

tags: ['loss']
date modified: Monday 27th March 2023, Mon
date created: Monday 27th March 2023, Mon
---

# Jensen Shannon Divergence Consistency Loss
- @linDivergenceMeasuresBased

- enforces smother neural network responses
- stable, consistent and insensitive across range of inputs
- $$
\mathcal{L}(p_{orig}, y)+ \lambda JS(p_{orig};p_{augmix1}; p_{augmix2})
$$
- $$
M = \frac{p_{orig}+p_{augmix1}+ p_{augmix2}}{3}
$$
- $$
JS(p_{orig}; p_{augmix1};p_{augmix2}) = \frac{1}{3}(KL[p_{orig}||M||]+KL[p_{augmix1}||M||]+KL[p_{augmix2}||M||])
$$



