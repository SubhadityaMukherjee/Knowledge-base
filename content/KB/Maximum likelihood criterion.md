---
title: Maximum likelihood criterion
toc: true
tags:
  - loss
date modified: Tuesday 27th August 2024, Tue
date created: Tuesday 27th August 2024, Tue
---

# Maximum likelihood criterion
```toc
```

Since each observed output should have high probability under its corresponding distribution $Pr(y_{i}|\theta_{i})$, we can choose the model params $\phi$ so they MAXIMIZE the combined probability across all I training examples
- ![](../images/Pasted%20image%2020240827214633.png)
- Assumptions
	- data are identically distributed
	- ![](../images/Pasted%20image%2020240827214708.png)
	- independent and identically distributed