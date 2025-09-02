---
title: Parameter Sharing for Graphs
toc: true
tags:
  - graph
date modified: Wednesday 30th October 2024, Wed
date created: Wednesday 30th October 2024, Wed
---

# Parameter Sharing for Graphs
```toc
```

## Parameter Sharing for Graphs

- We could learn a model with separate parameters associated with each node. However, now the network must independently learn the meaning of the connections in the graph at each position, and training would require many graphs with the same topology. 
- Instead, we build a model that uses the same parameters at every node, reducing the number of parameters and sharing what the network learns at each node across the entire graph
- One way to think of this is that each neighbor sends a message to the variable of interest, which aggregates these messages to form the update.
- ![[Pasted image 20241030114934.webp]]