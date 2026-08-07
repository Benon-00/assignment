# Function 8

## Function Name

```python
np.mean()
```

---

## Purpose

Describe what the function does.

_**Computes the arithmetic mean along a specified axis**_


## Syntax

```python
np.mean(a, axis=None, dtype=None, out=None, keepdims=<no value>, *, where=<no value>)
```

---

## Parameters

| Parameter | Required? (Yes/No) | Default Value | Expected Data Type | Description |
|-----------|---------------------|---------------|--------------------|-------------|
| a         | Yes                 | None          | array_like        |input array|
| axis         | No                 | None          | int, tuple of ints        |axis/axes along which the mean is computed|
| dtype         | No                 | None          | data-type        |Type used to compute the mean|
| out         | No                 | None          | ndarray        |Alternative output array|
| keepdims         | No                 | False          | bool        |Return reduced dimensions with size 1|
| where         | No                 | not set          | array_like bool    |Elements to include|


> **Questions to answer**
>
> - Which parameters are required?
_**a is required**_
> - Which parameters are optional?
_**axis, dtype, out, keepdims, where, are all optional**_
> - What happens if you omit an optional parameter?
_**mean is computed across al axes; dtype if inferred from the the array; not alternative output used**_
> - What default value is used?
_**None**_

---

## Return Value

What does the function return?

**_the mean, as a scalar when axis=None, or ndarray when axis is given_**

## Example

import numpy as np

arr = np.array([1,2,3,4,5])
print(np.mean(arr))

or 

matrix = np.array([[1,2,6], [4,8,12]]) #a
mask = (matrix % 2 == 0) #where
output_array = np.empty((2,1), dtype=np.float64) #keepdims & out

np.mean(
    a= matrix,
    axis=1, 
    dtype=np.float64, 
    out=output_array, 
    keepdims=True, 
    where=mask)

print(output_array)

## Expected Output

3.0

or

[[4.]
 [8.]]

## What did you learn about this function?

Write one or two sentences describing something interesting you discovered.

**it's easy to understand**