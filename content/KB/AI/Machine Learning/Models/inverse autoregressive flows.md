---
title: inverse autoregressive flows
toc: true
tags:
  - architecture
date modified: Tuesday 19th November 2024, Tue
date created: Tuesday 19th November 2024, Tue
---

# Inverse Autoregressive Flows
```toc
```
- A trick that allows fast learning and also fast (but approximate) sampling is to build a masked autoregressive flow to learn the distribution (the teacher) and then use this to train an inverse autoregressive flow from which we can sample eﬀiciently (the student)
- ![[af88b01525af98ecb305db72bd75c65d_MD5.webp]]