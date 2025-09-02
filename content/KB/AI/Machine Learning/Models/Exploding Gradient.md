---
toc: true
title: Exploding Gradient

tags: ['architecture']
date modified: Tuesday 7th February 2023, Tue
date created: Tuesday 7th February 2023, Tue
---

# Exploding Gradient

- weight matrices have max eigenvalue $max_{i} \lambda_{j} > 1$ , gradient increases per layer 
	- if enough depth, then converges to infinity 
- ![[Pasted image 20240930160935.webp]]
- ![[Pasted image 20240930160948.webp]]