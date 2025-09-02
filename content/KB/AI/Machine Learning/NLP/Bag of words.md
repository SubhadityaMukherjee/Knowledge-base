---
toc: true
title: Bag of words

tags: ['nlp']
date modified: Wednesday, December 7th 2022, 11:02:42 pm
date created: Wednesday, December 7th 2022, 11:00:14 pm
---

# Bag of Words


## Explained
- Count based conversion of document into fixed length vectors of integers
- `John likes to watch movies. Mary likes movies too.`
	- `[1, 2, 1, 1, 2, 1, 1, 0, 0, 0, 0]`
- `John also likes to watch football games. Mary hates football.`
	- `[1, 1, 1, 1, 0, 1, 0, 1, 2, 1, 1]`
- Order is arbitary

## Disadvantages
- Lose all info about word order
- Does not learn meaning of the words, so distance isnt very accurate
- Somewhat solved by [[Bag of n-grams]]
- [[Curse Of Dimensionality]]



