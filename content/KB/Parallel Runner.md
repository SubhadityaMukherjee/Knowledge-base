---
tags: ['temp']
toc: true
title: Parallel Runner
date modified: Monday, October 10th 2022, 2:02:20 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# Parallel Runner
```python
import random
import numpy as np
import concurrent
from typing import *
from concurrent.futures import ProcessPoolExecutor
from types import SimpleNamespace
import os
from pathlib import Path

def ifnone(a, b):
    """
    Return if None
    """
    return b if a is None else a


def listify(o):
    """
    Convert to list
    """
    if o is None:
        return []
    if isinstance(o, list):
        return o
    if isinstance(o, str):
        return [o]
    if isinstance(o, Iterable):
        return list(o)
    return [o]


def num_cpus() -> int:
    "Get number of cpus"
    try:
        return len(os.sched_getaffinity(0))
    except AttributeError:
        return os.cpu_count()


_default_cpus = min(16, num_cpus())
defaults = SimpleNamespace(
    cpus=_default_cpus, cmap="viridis", return_fig=False, silent=False
)


def parallel(func, arr: Collection, max_workers: int = None, leave=False):  # %t
    "Call `func` on every element of `arr` in parallel using `max_workers`."
    max_workers = ifnone(max_workers, defaults.cpus)
    if max_workers < 2:
        results = [
            func(o, i)
            for i, o in tqdm.tqdm(enumerate(arr), total=len(arr), leave=leave)
        ]
    else:
        with ProcessPoolExecutor(max_workers=max_workers) as ex:
            futures = [ex.submit(func, o, i) for i, o in enumerate(arr)]
            results = []
            for f in tqdm.tqdm(
                concurrent.futures.as_completed(futures), total=len(arr), leave=leave
            ):
                results.append(f.result())
    if any([o is not None for o in results]):
        return results

```



