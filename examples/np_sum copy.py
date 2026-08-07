# Function 7

## Function Name

```python
np.sum()
```

---

## Purpose

Describe what the function does.

_**Computes the sum of array elemts over a given axis (or all elements if o axis is specified)**_


## Syntax

```python
np.sum(a, axis=None, dtype=None, out=None, keepdims=<no value>, initial=<no value>, where=<no value>)
```

---

## Parameters

| Parameter | Required? (Yes/No) | Default Value | Expected Data Type | Description |
|-----------|---------------------|---------------|--------------------|-------------|
| a         | Yes                 | None          | array_like         |Elements to sum|
| axis      | No                 | None          | int, tuple of ints  |Axis/axes along which to sum; None sums all elements|
| dtype         | No                 | None          | data-type         |Type used for the summation|
| out         | No                 | None          | ndarray         |Alternative output array to place the results|
| keepdims         | No            | False (no value) | bool   |Retain reduced dimensions with size 1|
| initial         | No            | not set         | scalar   |starting value for the sum|
| where         | No            | not set | array_like bool   | ELements to include in the sum|

> **Questions to answer**
>
> - Which parameters are required?
_**a is required**_
> - Which parameters are optional?
_**axis, dtype, out, keepdims, initial, where, are all optional**_
> - What happens if you omit an optional parameter?
_**asummation occurs across all axis; the dtype is inferred from the array; no output array is reused**_
> - What default value is used?
_**axis=None; dtype=None; out=None**_

---

## Return Value

What does the function return?

**_either a _**

## Example

import numpy as np

arr = np.array([[3,4], [8,10]])
print(np.sum(arr))
print(np.sum(arr, axis=0))
print(np.sum(arr, axis=1))

or 

matrix = np.array([[1,2,3], [4,5,6]]) #a
mask = matrix > 0 #where
output_array = np.empty((1,3), dtype=np.float64) #keepdims & out

np.sum(
    a= matrix,
    axis=0, 
    dtype=np.float64, 
    out=output_array, 
    keepdims=True, 
    initial=10, 
    where=mask)

print(output_array)

## Expected Output

25
[11 14]
[ 7 18]

or

[[15. 17. 19.]]


## What did you learn about this function?

Write one or two sentences describing something interesting you discovered.

**eager to find out how to apply it**