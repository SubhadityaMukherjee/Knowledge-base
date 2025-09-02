---
title: Benchmark Data Repositories for Better Benchmarking
toc: true
tags:
  - benchmark
date modified: Wednesday 9th October 2024, Wed
date created: Wednesday 9th October 2024, Wed
---

# Benchmark Data Repositories for Better Benchmarking
```toc
```

- Benchmark Data Repositories for Better
- Benchmarking
- comparatively less attention has been paid to the repositories where
- these datasets are stored, documented, and shared
## Introduction
- Benchmarking can help quantify
- progress on these tasks over time, and the availability of a well-studied, standard task evaluation
- environment can be a critical first step before moving to real-world applications, especially in high-
- stakes or expensive domains.
- Early data repositories, such as the UCI ML Repository, arose to address the data needs that come
- with ML benchmarking
- the process of selecting a dataset is often less about a scientific or engineering application and more
- about the compositional characteristics of the data and its associated tasks, for which a particular
- class of methods is applicable
- benchmark repository
- to describe repositories that support the discovery and use of datasets for evaluating ML models
## Valuing Datasets as Research Contributions
## Dataset Citations and Metrics
- persistent identifier (PID), such as a DOI, that can reliably
- be used to access a dataset has been widely recommended by experts
- ML
- datasets and their documentation frequently lack PIDs and are often only available via GitHub or
- personal/research group websites
- In ML, however, datasets are often referred
- to using combinations of names, descriptions, and associated papers, which can be challenging to
- disambiguate
- include the minted DOI
## Connection Metadata
- connects a dataset to associated research entities (such as the dataset's creators or
- maintainers, publications, code, or other datasets)
- Introductory papers can give the data a story beyond standardized documentation, providing useful context about the problem,
- background on data collection procedures, and guidance about tasks for which the data have already
- been used.
- Introductory papers can be included in benchmark repositories as a
- standardized metadata field
- dataset's point of contact:
- someone responsible for answering questions about the dataset and addressing any issues
- lthough long-term data maintenance, and determining different
- stakeholders' responsibilities in that maintenance, remain challenging tasks \[28, 60, 61\], establishing
- a point of contact can help prevent the development of a disconnect between a dataset and its creators,
- which is not uncommon in ML
## Dataset Licenses
- Data repositories can include licenses as part of a dataset's metadata.
- it
- is ambiguous if models trained on a dataset count as "derivative work"
- current licensing practices for ML datasets are often irregular,
- conflicting, poorly documented, or over-permissive given the dataset content
## Addressing Issues with Dataset Content
- technical flaws such as labeling errors and annotation artifacts
- privacy
- and copyright violations
- inclusions of hate speech or other harmful content
- representational biases
- miscellaneous ethical issues
## Contextual Metadata
- including information about a dataset's
- source, funding, collection, annotation, and preprocessing, benchmark repositories can illuminate the
- assumptions and motivations of dataset creators and flag potential dataset issues
- Data Cards
- datasheets
- Dataset Nutrition Label
- FAIR principles
- Data selection, filtering, and annotation processes are important design decisions that can significantly
- impact downstream performance \[7, 38, 75, 100, 101\]; however, they tend to be under-documented
## Quality Review
- datasets containing personally identifiable information should not be released
- Benchmark repositories can help
- identify these problems throughout the data lifecycle by (1) performing a pre-release quality review
- \[92\] to catch issues before a dataset is shared, and (2) by serving as a centralized location to collect
- users' reports and concerns \[72\] to flag issues throughout a dataset's use and reuse
- It is an open
- question to what extent repositories should be involved in these decisions; several popular repositories
- (e.g., Zenodo, Mendeley, etc.) view their role as only providing infrastructure and not conducting any
- kind of data review.
## Dataset Revision and Deprecation
- dataset revision by documenting data versions and connecting
- each dataset to a responsible point of contact
- can enforce versioning by assigning a new version number
- whenever a data file is changed.
- deprecation of datasets.
- creators often withdraw their dataset without an explanation of why it
- was withdrawn or explicit instructions not to use the dataset
- deprecation reports are posted in a scattered, decentralized manner via news articles,
- conference papers, or researcher or lab websites
- it can be unclear to researchers if a
- dataset is acceptable to use; it is not uncommon for datasets to remain in use after their deprecation,
- including in published, peer-reviewed papers
- If a deprecation report is clearly displayed in the same place where a dataset was available, it
- clarifies to researchers (and reviewers) that the dataset should not be used
## Compositional and Task Metadata
- Compositional metadata
- describe the makeup of a dataset,
- Croissant
- Task metadata
- include the intended or appropriate ML tasks for a dataset (e.g., image classification
- or time-series prediction) and specialized metadata relevant to those tasks
- As an example, HuggingFace Datasets
- \[17\], which specializes in NLP data, collects metadata on language and multilinguality, text creation,
- and fine-grained NLP tasks
- repositories can require that data
- donors provide high-quality compositional and task metadata, including specialized task metadata,
- where appropriate
## Benchmark Metadata
- if a repository displays a
- particular benchmarked result for a dataset, they should ensure that specific details on all settings
- and hyperparameter values used to obtain that result are available
## Encouraging Holistic Evaluation
- Kaggle \[18\]
- and Papers with Code
- Leaderboarding
- Further, as measures
- of uncertainty are seldom incorporated, seemingly record-breaking performance improvements are
- not always statistically significant
## Analysis Beyond Single Metrics
- variety of metrics, capturing model size and
- complexity, energy consumption, inference latency, and the amount of data used
- error analysis or disaggregated evaluations
## Metric Uncertainty
- Metrics shown without any measure of uncertainty can prompt fallacious conclusions, e.g., that
- one model performs definitively better than another
- Instead, including uncertainty makes these
- benchmarked results more informative \[1, 157\], and a growing body of methodologies have been
- developed for estimating uncertainty, computing confidence intervals, and performing statistical
- significance testing in the context of model comparison
- variance, uncertainty, and statistical significance
- in model analysis
## Living Datasets
- leaderboards can evaluate submitted models
- on a private, hitherto unused test set \[167--169\] (e.g., as done by Kaggle) or on out-of-distribution
- data
- eaderboards can also support "living" or evolving datasets,
- to which dataset creators continuously add new examples or tasks and remove outdated or erroneous
- examples.
- benchmarked performances of two models evaluated at two
- different points in time may not be directly comparable
- robust models will generally outperform those using a specific trick or artifact as
- evaluations are repeated over time
- de-incentivizing
- overfitting and helping bridge the gap between benchmarked and real-world performance.
## Dataset Discoverability
- there also exists a plethora
- of other high-quality datasets that could have been used but did not win the "benchmark lottery"
- existing standards emphasize
- the importance of standardized, rich metadata \[39, 129, 130\], which enable searching for datasets
- via keywords, filtering, and controlled vocabularies
- search based on compositional and task
- metadata
- UCI ML Repository's search functionality includes a filter
- for classification, regression, clustering, or other datasets.