---
toc: true
title: croissant
tags:
  - dataset
date modified: Tuesday 25th June 2024, Tue
date created: Tuesday 25th June 2024, Tue
---

# Croissant

- Croissant is a metadata description format
- Ml datasets are a combination of structured and unstructured data, which make them complicated to manage
- Croissant was built on top of schema.org, and has more details relative to it
- The format has 4 layers
	- dataset level metadata
	- resource description
	- content structure
	- ml semantics
- Croissant does not require any changes to underlying data
- Analysis and visualization tools work out of the box for all datasets
- Using croissant, datasets can be exposed consistently throughout platforms
- Collaborations with google, huggingface, google dataset search also exist
- openml has deeper dataset description by default, slightly lesser in HF and kaggle
- once loaded, datasets can be imported elsewhere (torch, tf etc) easily
- Croissant editor - web app where you can use a GUI to enter the dataset descriptions
- NeurIPS also now recommends using the Croissant format
