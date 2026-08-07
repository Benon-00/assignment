# Function 6

## Function Name

```python
np.reshape()
```

---

## Purpose

Describe what the function does.

_**Gives a new shape to an array without changing its data**_


## Syntax

```python
np.reshape(a, newshape, order='C')
```

---

## Parameters

| Parameter | Required? (Yes/No) | Default Value | Expected Data Type | Description |
|-----------|---------------------|---------------|--------------------|-------------|
| a         | Yes                 | None          | array_like        |Array to be reshaped|
| newshape  | Yes                 | None          | int or tuple of ints  |New shape (must be compatible with original size)|
| order         | No              | 'C'           | {'C','F','A' }       |Order to read/place elements|

> **Questions to answer**
>
> - Which parameters are required?
_**a, newshape are required**_
> - Which parameters are optional?
_**Order is optional**_
> - What happens if you omit an optional parameter?
_**defaults to a row-major C-style order**_
> - What default value is used?
_**order='C'**_

---

## Return Value

What does the function return?

**_the new shape of the ndarray_**

## Example

import numpy as np

arr = np.arange(6)  
reshaped = np.reshape(arr, (2,3))
print(reshaped)

## Expected Output

[[0 1 2]
 [3 4 5]]

## What did you learn about this function?

Write one or two sentences describing something interesting you discovered.

**A classic real-world application for np.reshape is flattening a multi-dimensional matrix into a 1D vector (or vice versa) for Machine Learning model compatibility.**