---
toc: true
title: Hopfield networks

tags: ['architecture']
date modified: Monday, October 10th 2022, 2:02:25 pm
date created: Thursday, July 28th 2022, 5:59:06 pm
---

# Hopfield Networks
- [from](https://publish.obsidian.md/fabian-groeger/Machine+Learning+%26+Deep+Learning/Deep+Learning/Architectures/Hopfield+Networks)
- Older architecture used to store and retrieve patterns
- Building blocks
    - Data (list of patterns)
    - Network
        - Nodes
        - All nodes are connected with each other
    - Retrieval
        - Input: partial pattern
        - Output: full pattern (retrieved)
            - "best match" partial pattern to entire data
            - Filling out the missing nodes with the best pattern is called _update rule_
    - Energy Function
        - Theoretical concept, similar to a loss function
        - Is not being optimized directly but trough update function
    - Update function
        - Optimizes the pattern that will be retrieved to best match the partial pattern
- ![[a1478a6107623b3712ae0477c54bbf51_MD5.webp]]