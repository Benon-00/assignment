# Function 11

## Function Name

```python
np.sort()
```

---

## Purpose

Describe what the function does.

_**Reurns a sorted copy of an array**_


## Syntax

```python
np.sort(a, axis=-1, kind=None, order=None)
```

---

## Parameters

| Parameter | Required? (Yes/No) | Default Value | Expected Data Type | Description |
|-----------|---------------------|---------------|--------------------|-------------|
| a         | Yes                 | -          | array_like        |Array to sort|
| axis         | No                 | -1          | int or None       |Axis to sort along: None flattens the array first|
| kind         | No                 | None ('quicksort')  |{'quicksort','mergesort','heapsort','stable'}        |Sorting algorithm|
| order        | No                 | None         | str or list of str        |Field(s) to order by, for structured arrays|

> **Questions to answer**
>
> - Which parameters are required?
_**a is required**_
> - Which parameters are optional?
_**axis, kind, order; are all optional**_
> - What happens if you omit an optional parameter?
_**axis defaults to -1; kind defaults to None; order defaults to None**_
> - What default value is used?
_**axis=-1; kind=None; order=None**_

---

## Return Value

What does the function return?

**_float radians_**

## Example

import numpy as np

arr = np.array([1,4,7,2,5,10])

sorted = np.sort(
    a = arr,
    axis = None,
    kind = None,
    order = None
)
print(sorted)


## Expected Output

[ 1  2  4  5  7 10]
## What did you learn about this function?

Write one or two sentences describing something interesting you discovered.

**easy to understand!**