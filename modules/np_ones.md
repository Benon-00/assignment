# Function 3

## Function Name

```python
np.ones()
```

---

## Purpose

Describe what the function does.

_**Reurns a new array of a given shape and type, filled with ones**_


## Syntax

```python
np.ones(shape, dtype=None, order='C', *, like=None)
```

---

## Parameters

| Parameter | Required? (Yes/No) | Default Value | Expected Data Type | Description |
|-----------|---------------------|---------------|--------------------|-------------|
| shape     | Yes                 | None          | int/tuple of ints  |Shape of the new array|
| dtype     | No                 | None(resolves to float64  | data-type          |Desired data type|
| order     | No                 | 'C'            | 'C','F'          |Memory layout order: Row-major (C) or column-major (Fortan) order|
| like      | No                  | None           | array_like          |Reference object for array creation protocol|



> **Questions to answer**
>
> - Which parameters are required?
_**shape is required**_
> - Which parameters are optional?
_**dtype, order, like are all optional**_
> - What happens if you omit an optional parameter?
_**dtype defualts to np.float64; order defaults to row major 'C' order; and the like reference object is not permitted**_
> - What default value is used?
_**dtype=np.float64; order='C', like=None**_

---

## Return Value

What does the function return?

**_an ndarray of ones with the given shape and dtype_**

## Example

import numpy as np

base_data = ((2,3))
custom_array = np.ones(
    shape=base_data, 
    dtype=np.int32, 
    order='C', 
    like=None)

print(custom_array)

## Expected Output

[[1 1 1]
 [1 1 1]]

## What did you learn about this function?

Write one or two sentences describing something interesting you discovered.

**also need explaination on how to use it**