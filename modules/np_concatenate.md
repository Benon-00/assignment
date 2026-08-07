# Function 9

## Function Name

```python
np.concatenate()
```

---

## Purpose

Describe what the function does.

_**Joins a sequence of arrays along an existing axis**_


## Syntax

```python
np.concatenate((a1, a2,....), axis=0, out=None, dtype=None, casting="same_kind")
```

---

## Parameters

| Parameter | Required? (Yes/No) | Default Value | Expected Data Type | Description |
|-----------|---------------------|---------------|--------------------|-------------|
| (a1, a2...)   | Yes             | None          | sequence of array_like |Arrays to join; must have same shape except along axis|
| axis  | No           |0          | int or None  |Axis along which to join; None flattens arrays first|
| out  | No           |None          | ndarray  |Output array to store the results|
| dtype  | No         |None          | data-type  |Output data type|
| Casting  | No           |"same_kind" | str  | Controls type casting behaviour|

> **Questions to answer**
>
> - Which parameters are required?
_**(a1, a2...) sequence of arrays is required**_
> - Which parameters are optional?
_**axis, out, dtype, casting; are all optional**_
> - What happens if you omit an optional parameter?
_**arrays are joined at axis=0; dtype inferred from input values; there's no repeating output array**_
> - What default value is used?
_**axis=0; out=None; dtype=None; casting="same_kind"**_

---

## Return Value

What does the function return?

**_a new ndarray formed by joining the input arrays_**

## Example

import numpy as np

a = np.array([[1, 2]])
b = np.array([[3, 4]])
print(np.concatenate((a, b), axis=0))

or

a1 = np.array([[10,20], [30,40]], dtype=np.int32)
a2 = np.array([[50, 60]], dtype=np.int32)

output_array = np.empty((3,2), dtype=np.float32)

results = np.concatenate(
    (a1, a2),
    axis=0,
    out=output_array,
    casting="same_kind"
)

print(results)

## Expected Output

[[1 2]
 [3 4]]

 or

[[10. 20.]
 [30. 40.]
 [50. 60.]]

## What did you learn about this function?

Write one or two sentences describing something interesting you discovered.

**one has to be keen while using it**