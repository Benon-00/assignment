# Functiom 2

## Function Name

```python
np.zeros()
```

---

## Purpose

Describe what the function does.

_**Reurns a new array of a given shpae and typr, filled with zeros**_


## Syntax

```python
np.zeros(shape, dtype=float, order='C', *, like=None)
```

---

## Parameters

| Parameter | Required? (Yes/No) | Default Value | Expected Data Type | Description |
|-----------|---------------------|---------------|--------------------|-------------|
| shape     | Yes                 | None          | int/tuple of ints  |Shape of the new array|
| dtype     | No                 | float          | data-type          |Desired data type|
| order     | No                 | 'C'            | 'C','F'          |Row-major (C) or column-major (Fortan) order|
| like      | No                  | None           | array_like          |Reference object for array creation protocol|



> **Questions to answer**
>
> - Which parameters are required?
_**shape is required**_
> - Which parameters are optional?
_**dtype, order, like optional**_
> - What happens if you omit an optional parameter?
_**dtype defualts to np.float64; order defaults to row major 'C' order; and the like reference object is not permitted**_
> - What default value is used?
_**dtype=np.float64; order='C', like=None**_

---

## Return Value

What does the function return?

**_nd array of zeros with given shape and dtype_**

## Example

import numpy as np

base_data = ((2,3))
custom_array = np.zeros(
    shape=base_data, 
    dtype=np.float32, 
    order='F', 
    like=None)

print(custom_array)

## Expected Output

[[0. 0. 0.]
 [0. 0. 0.]]

## What did you learn about this function?

Write one or two sentences describing something interesting you discovered.

**this one, i definetely need explaination on what's happening**