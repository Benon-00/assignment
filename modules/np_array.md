# Function 1

## Function Name

```python
np.array()
```

---

## Purpose

Describe what the function does.

_**Creates a Numpy array (ndarray) from a python list, tuple or other array-like object**_
_**usually imported as import numpy as np**_

## Syntax

```python
np.array(object, dtype=None, copy=True, order='K', subok=False, ndmin=0)
```

---

## Parameters

| Parameter | Required? (Yes/No) | Default Value | Expected Data Type | Description |
|-----------|---------------------|---------------|--------------------|-------------|
| object    | Yes                 | None          | array-like        |Inut data (list, tuple, nested sequence, etc)|
| dtype    | No                 | None          | data-type        |desired data tyoe of array elements|
| copy    | No                 | True          | boolean        |Whether to copy the object|
| order    | No                | 'K'          | 'K','A','C','F'        |Memory layour order|
| subok    | No                | False          | boolean        |Whether to allow subclasses of ndarray|
| ndmin    | No                 | 0          | int        | Minimum number of dimensions of the result|


> **Questions to answer**
>
> - Which parameters are required?
_**object is required**_
> - Which parameters are optional?
_**dtype, copy, order subok, ndmin are all optional**_
> - What happens if you omit an optional parameter?
_**the optional parameters defaults are used, i.e dtype is inferred from data-array; the array object is copied(True); the order layout ik 'K'; no subclasses allowed, no minimum dimesnions enforced**_
> - What default value is used?
_**dtype=None; Copy=True; order='K'; subok=False, ndmin=0**_

---

## Return Value

What does the function return?

**_the list ndarray containing the input data_**

## Example

import numpy as np

array = np.array([2,3,4,5,6])

print(array)
print(array.dtype)


## Expected Output

[2 3 4 5 6] 
int64

## What did you learn about this function?

Write one or two sentences describing something interesting you discovered.

**it's easy to understand**