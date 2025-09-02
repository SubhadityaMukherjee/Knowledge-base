---
toc: true
title: Beam search

tags: ['architecture']
date modified: Monday, October 10th 2022, 2:02:33 pm
date created: Thursday, July 28th 2022, 5:59:06 pm
---

# Beam Search
- ![[Pasted image 20220810155603.webp]]
- ([from](https://publish.obsidian.md/fabian-groeger/Machine+Learning+%26+Deep+Learning/Deep+Learning/Architectures/RNN/Beam+Search))
- at each step, keep track of the k mos probable translation hypotheses (k, beam size)
- examine the k most probable words for each hypothesis, compute their entire scores, keep k best ones
- not guaranteed to find optimal solution, but more efficient than exhaustive search
- it does not only take the best word, it rather takes the best B (user specified) and generates multiple hypothesis, which will then be evaluated and the best one at each step is chosen for the next ones
- not guaranteed to find the optimal solution and is therefore an approximate search
- problems:
    - when multiplying a lot of probabilities of very unlikely word (e.g. almost 0 but not exactly), the result will get very small and the system can no longer represent it. results in numerical underflow --> instead of multiplying, summing the log of probabilities (more numerical stable)
    - if the sentence is very long, the probabilities get very low, therefore it rather takes smaller translations --> normalize the output by the number of word in the translation (average of the log of each word)
- how to choose beam width $B$?
    - the smaller, the fewer probabilities are considered (worse result, faster)
    - the larger, the more are considered, but the more computing expensive it is (better results, slower)
    - try out different values and cross check



