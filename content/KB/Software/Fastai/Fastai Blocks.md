---
toc: true
title: Fastai Blocks

tags: ['deeplearning']
date modified: Monday, October 10th 2022, 2:02:28 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# [fastai](fastai.md) Blocks

## Building Blocks
```python
# Image Classification
dls = DataBlock(
    blocks=(ImageBlock, CategoryBlock), 
    get_items=get_image_files, 
    splitter=RandomSplitter(valid_pct=0.2, seed=42),
    get_y=parent_label,
    item_tfms=[Resize(192, method='squish')]
).dataloaders(path)

dls.show_batch(max_n=6)
learn = cnn_learner(dls, resnet18, metrics=error_rate)
learn.fine_tune(8)
```

```python
# Label regex
pets = DataBlock(blocks = (ImageBlock, CategoryBlock),
                 get_items=get_image_files, 
                 splitter=RandomSplitter(seed=42),
                 get_y=using_attr(RegexLabeller(r'(.+)_\d+.jpg$'), 'name'),
                 item_tfms=Resize(460),
                 batch_tfms=aug_transforms(size=224, min_scale=0.75))
dls = pets.dataloaders(path/"images")
```

- DataBlock is more general
	- list models

```python
timm.list_models('convnex*')
```

```python
# Segmentation
path = untar_data(URLs.CAMVID_TINY)
dls = SegmentationDataLoaders.from_label_func(
    path, bs=8, fnames = get_image_files(path/"images"),
    label_func = lambda o: path/'labels'/f'{o.stem}_P{o.suffix}',
    codes = np.loadtxt(path/'codes.txt', dtype=str)
)
learn = unet_learner(dls, resnet34)
learn.fine_tune(8)
```

- Segmentation Dataloaders is just another abstraction of the DataBlock for a specific case. Can use the DataBlock as well

```python
# Tabular
dls = TabularDataLoaders.from_csv(path/'adult.csv', path=path, y_names="salary",
    cat_names = ['workclass', 'education', 'marital-status', 'occupation', 'relationship', 'race'],
    cont_names = ['age', 'fnlwgt', 'education-num'],
    procs = [Categorify, FillMissing, Normalize])
learn = tabular_learner(dls, metrics=accuracy)
learn.fit_one_cycle(2)
```

- [Fitting](Fitting.md) because pretrained models are not going to be there

```python
# Collaborative [Filtering](Filtering.md)
dls = CollabDataLoaders.from_csv(path/'ratings.csv')
learn = collab_learner(dls, y_range=(0.5,5.5))
learn.fine_tune(8)
```

- Range is for the output (Since its not a binary output)
- Saving a model

```python
learn.export('model.pkl')
```



