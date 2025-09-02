---
toc: true
title: Dreamfusion
tags: ['architecture']
---

## Dreamfusion
- text-to-3D model
- uses a pretrained 2D text-to-image difusion model to perform textto-3D synthesis
- Dreamfusion replaces previous CLIP techniques with a loss derived from distillation of a 2D difusion model
- the difusion model can be used as a loss within a generic continuous optimization problem to generate samples
- sampling in parameter space is much harder than in pixels as we want to create 3D models that look like good images when rendered from random angles
- this model uses a diferentiable generator - Other approaches are focused on sampling pixels, however, this model instead focuses on creating 3D models that look like good images when rendered from random angles



