# Function 7

## Function Name

```python
plt.subplots()
```

---

## Purpose

Describe what the function does.

_**Creates a figure and a grid of subplots (Axes) in one call; the standard way to set up multi-panel figures**_


## Syntax

```python
plt.subplots(nrows=1, ncols=1, figsize=None, sharex=False, sharey=False, **kwargs)
```

---

## Parameters

| Parameter | Required? (Yes/No) | Default Value | Expected Data Type | Description |
|-----------|---------------------|---------------|--------------------|-------------|
|nrows      | No                  | 1             | int          |Number of subplot rows|
|ncols      | No                  | 1             | int          |Number of subplot columns|
|figsize    | No                  | rcParams default (6.4, 4.8)   |tuple(w,h in inches)|Figure size|
|sharex     | No                  | False         | bool/str      |Share x-axis across subplots|
|sharey     | No                  | False         | bool/str      |Share y-axis across subplots|
|dpi        | No                  | rcParams default (100)        |float    | Resolution |




> **Questions to answer**
>
> - Which parameters are required?
_**none is required (all have defaults)**_
> - Which parameters are optional?
_**all are optional**_
> - What happens if you omit an optional parameter?
_**they use their default values**_
> - What default value is used?
_**nrows=1; ncols=1; figsize=(6.4, 4.8); sharex=False; sharey=False; dpi=100**_

---

## Return Value

What does the function return?

**the subplots in one canvas i.e can be 10 subplots in a 5x5 canvas etc**

## Example

import numpy as np

fig, axs = plt.subplots(2, 2, figsize=(10, 4))

# Indexing as [row, column]
axs[0, 0].plot([1, 2, 3])                           # Top-left
axs[0, 1].bar(['a', 'b'], [3, 5])                     # Top-right
axs[1, 0].scatter([3, 7, 8, 9], [0.4, 0.7, 0.9, 0.1]) # Bottom-left
axs[1, 1].hist([3, 7, 8, 9], align='mid', cumulative=True)  # Bottom-right
plt.show()


## Expected Output

4 subplots: one line graph, one bar chart, one scatter plot and one histogram

## What did you learn about this function?

Write one or two sentences describing something interesting you discovered.

**i just realized this makes work very easy i.e plotting hundreds of graphs into 10 subplots (each having 10 graphs)**