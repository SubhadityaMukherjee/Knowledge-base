---
toc: true
title: Galactica
tags: ['architecture']
---

## Galactica
- new large model for automatically organizing science developed by Meta AI and Papers with Code
- ability to train on it for multiple epochs without overfitting, where upstream and downstream performance improves with use of repeated token
- The dataset design is critical to the approach as all of it is processed in a common markdown format to blend knowledge between sources.
- Citations are processed via a certain token that allows researchers to predict a citation given any input context
- The capability of the model of predicting citations improves with scale and the model becomes better at the distribution of citations
- the model can perform multi-modal tasks involving SMILES chemical formulas and protein sequences
- transformer architecture in a decoder-only setup with GeLU activation for all model sizes.



