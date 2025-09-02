---
tags: ['temp']
date created: Thursday, August 11th 2022, 12:32:22 am
date modified: Monday, October 10th 2022, 2:02:32 pm
---

# Broadcasting
- Expanding the shape of an operand in a matrix math operation to dimensions compatible for that operation. For instance, linear algebra requires that the two operands in a matrix addition operation must have the same dimensions. Consequently, you can't add a matrix of shape (m, n) to a vector of length n. Broadcasting enables this operation by virtually expanding the vector of length n to a matrix of shape (m,n) by replicating the same values down each column.



