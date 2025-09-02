---
toc: true
title: Phrase Representation Learning

tags: ['architecture']
date modified: Monday, October 10th 2022, 2:02:20 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# Phrase Representation Learning
- [Learning Phrase Representations Using RNN Encoder–Decoder for Statistical Machine Translation](https://www.aclweb.org/anthology/D14-1179/)
- two [Recurrent](Recurrent.md) neural networks [Basic RNN Architectures](Basic%20RNN%20Architectures.md) that is together able to learn the mapping from a sequence of an arbitrary length to another sequence, possibly from a different set, of an arbitrary length.
- either score a pair of sequences (in terms of a conditional [Probability](Probability.md)) or generate a target sequence given a source sequence
- jointly trained to maximize the conditional [Probability](Probability.md) of a target sequence given a source sequence
- reset gate and an update gate that adaptively control how much each hidden unit remembers or forgets while reading/generating a sequenc
- RNN Encoder–Decoder to score each phrase pair in the phrase table
- capture linguistic regularities in the phrase pairs well
- [BLEU](BLEU.md)



