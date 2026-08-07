# Function 10

## Function Name

```python
np.where()
```

---

## Purpose

Describe what the function does.

_**Reurns elements chosen from two arrays depending on a condition (or returns indices where a condition is True, when used with only one argument)**_


## Syntax

```python
np.where(condition, x=<no value>, y=<no value>)
```

---

## Parameters

| Parameter | Required? (Yes/No) | Default Value | Expected Data Type | Description |
|-----------|---------------------|---------------|--------------------|-------------|
| condition     | Yes             | None          | array_like of bool |Where True, yield x, otherwise yield y|
| x     | No(but required to gether with y) | not set | array_like |Values to use when condition is True|
| y     | No(but required to gether with x) | not set | array_like |Values to use when condition is False|

> **Questions to answer**
>
> - Which parameters are required?
_**condition is required**_
> - Which parameters are optional?
_**x, y areoptional, but have to be used together**_
> - What happens if you omit an optional parameter?
_**the function behaves like np.asarray(condition).nonzero(), returning indices where the condition is True**_
> - What default value is used?
_**no defaults, omitting x/y changes the return type entirely (indices vs values)**_

---

## Return Value

What does the function return?

**_an ndarray of selected elements if x,y are given; or a tuple of index arrays if only the condition is given_**

## Example

import numpy as np

arr = np.array([1, 2, 3, 4, 5])
result = np.where(arr > 2, arr, 0)
print(result)

<!-- or -->

arr = np.array([1, 2, 3, 4, 5])
result = np.where(arr > 2)
print(result)

## Expected Output

[0 0 3 4 5]

<!-- or -->

(array([2, 3, 4]),)

## What did you learn about this function?

Write one or two sentences describing something interesting you discovered.

**it's easy to visualize where it'll be used**