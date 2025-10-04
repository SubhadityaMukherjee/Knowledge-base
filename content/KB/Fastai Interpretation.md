---
toc: true
title: Fastai Interpretation

tags: ['deeplearning']
date modified: Monday, October 10th 2022, 2:02:28 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# [fastai](fastai.md) Interpretation

## Classification Interpretation
```python
interp = ClassificationInterpretation.from_learner(learn)
interp.plot_confusion_matrix()
interp.plot_top_losses(5, nrows=1)
```

- Ordered by loss
- If predicted correctly but still shown, then low confidence

## Cleaner
```python
cleaner = ImageClassifierCleaner(learn)
cleaner

for idx in cleaner.delete(): cleaner.fns[idx].unlink()
for idx,cat in cleaner.change(): shutil.move(str(cleaner.fns[idx]), path/cat)
```

## Get All Classes and Their Probabilities
```python
def classify_image(img):
	pred,idx,probs = learn.predict(img)

return dict(zip(categories, map(float,probs)))

classify_image(im)
```



