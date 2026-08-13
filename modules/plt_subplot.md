# Function 18

## Function Name

```python
plt.subplot()
```

---

## Purpose

Describe what the function does.

_**adds a single subplot to the current figure using a 3-digit or explicit grid position(older/simpler alternative to subplots())**_

## Syntax

```python
plt.subplot(*args, **kwargs)
```

---

## Parameters

| Parameter | Required? (Yes/No) | Default Value | Expected Data Type | Description |
|-----------|---------------------|---------------|--------------------|-------------|
|nrows   |Yes*   |None | int   |Number of rows in grid|
|ncols   |Yes*   |None | int   |Number of columns in grid|
|index   |Yes*   |None | int   |Position of this subplot (1-indexed)|
|projection |No   |None (rectilinear) | str   |eg. 'polar', '3d'|

*Can be passed as threee separate ints or a single 3-digit int (e.g plt.subplot(2, 2, 1)==plt.subplot(221))

> **Questions to answer**
>
> - Which parameters are required?
_**nrows, ncols, index; are all required**_
> - Which parameters are optional?
_**projection, sharex, sharey**_
> - What happens if you omit an optional parameter?
_**creates a standard rectilinear (linear-scale Cartesian) Axes**_
> - What default value is used?
_**projection=None**_

---

## Return Value

What does the function return?

**a subplot having the defined rows,columns**

## Example

import matplotlib.pyplot as plt

plt.subplot(1, 3, 1)
plt.plot([1,2,3])
plt.subplot(1, 3, 2)
plt.bar(['a','b'], [3,5])
plt.show()


## Expected Output
**a subplot having 1 row, 3 columns, and 2 charts indexed at position 1 & 2, with position 3 having an empty space*

## What did you learn about this function?

Write one or two sentences describing something interesting you discovered.

**i can start to see their uses, compared to plt.subplots*



