---
title: Data storage for different AI dataset services
toc: true
tags:
  - dataset
date modified: Friday 27th September 2024, Fri
date created: Friday 27th September 2024, Fri
---

# Data Storage for Different AI Dataset Services
```toc
```
- [Analyze data sharing platforms](https://github.com/openml/meta/issues/13)
- [[Benchmark Data Repositories for Better Benchmarking]]
## Template
- How do they store data?
	- blank
- Why is it useful?
	- blank
- Data upload interface
- Data view interface

## Kaggle
- They started with datasets, and then moved on to other things
- How do they store data?
	- Pretty much anything, but usually a folder with files and metadata
- Why is it useful?
	- competitions
	- they were the pretty much the first ones in this space
	- community features (likes etc)
- Data upload interface
	- ![[Pasted image 20241007164815.webp]]
	- ![[Pasted image 20241007164830.webp]]
- Data view interface
	- ![[Pasted image 20241007164801.webp]]
## Hugging Face
- Started with models, integrated with deep learning libraries. they took advantage of the rise in transformer libraries and then supported all of the ones since
- How do they store data?
	- Folder of parquet files , with the occasional metadata csv
- Why is it useful?
	- easy to view the dataset directly without downloading
	- spaces to run the data directly
	- directly copy API command
	- many papers published
	- github LFS upload and discussions
	- community features (likes etc)
- Data upload interface
	- ![[Pasted image 20241007163745.webp]]
	- ![[Pasted image 20241007163823.webp]]
- Data view interface
	- ![[Pasted image 20241007163555.webp]]

## [NCBI](https://www.ncbi.nlm.nih.gov/gene?LinkName=geoprofiles_gene&from_uid=78694385) (Bio Tech info)
- Specific biotech data
- How do they store data?
	- A tab delimited file : DataSet SOFT (but saved as a .gz archive)
- Why is it useful?
	- Specific data views : eg genes
- Data view interface
	- ![[Pasted image 20241007165737.webp]]
	- ![[Pasted image 20241007165755.webp]]

## [U.S. Department of Energy Office of Scientific and Technical Information](https://www.osti.gov/dataexplorer/) (Physics)
- How do they store data?
	- Images are in .zip, tabular in .csv and metadata as .xml
- Why is it useful?
- Data upload interface
- Data view interface

## Interesting Features for Us
- Community features - likes, comments 
- Notebooks
- Directly copy API command
- More PR ( implementations of recent datasets/models etc)