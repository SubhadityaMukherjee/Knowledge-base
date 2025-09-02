---
toc: true
title: Fasai Tricks

tags: ['deeplearning']
date modified: Monday, October 10th 2022, 2:02:28 pm
date created: Friday, July 29th 2022, 4:06:12 pm
---

# Fasai Tricks

## Batched Map
```python
tok_ds = ds.map(tok_func, batched=True)
```

## Learning Rate Finder
```python
learn.lr_find(suggest_funcs=(slide, valley))
```

## Test Dataset
```python
tst_dl = learn.dls.test_dl(tst_df)
preds,_ = learn.get_preds(dl=tst_dl)
```

## Ensemble
```python
def ensemble():
    learn = tabular_learner(dls, metrics=accuracy, layers=[10,10])
    with learn.no_bar(),learn.no_logging(): learn.fit(16, lr=0.03)
    return learn.get_preds(dl=tst_dl)[0]
learns = [ensemble() for _ in range(5)]

ens_preds = torch.stack(learns).mean(0) # stack and mean
```



