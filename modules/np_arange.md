# Function 4

## Function Name

```python
np.arange()
```

---

## Purpose

Describe what the function does.

_**Reurns evenly spaced values within a given interval**_


## Syntax

```python
np.arange([start, ]stop, [step, ]dtype=None, *, like=None)
```

---

## Parameters

| Parameter | Required? (Yes/No) | Default Value | Expected Data Type | Description |
|-----------|---------------------|---------------|--------------------|-------------|
| start     | Yes                 | 0              | number             |start of interval (inclusive)|
| stop      | Yes                 | -              | number             |end of interval (exclusive)|
| step      | No                  | 1              | number             |spacing between values|
| dtype     | No                  | inferred from the array           | data-type          |Type of output array; inferred if not given|
| like     | No                  | None            | array_like         |Reference object for array creation protocol|

> **Questions to answer**
>
> - Which parameters are required?
_**start/stop are required**_
> - Which parameters are optional?
_**step, dtype, like are all optional**_
> - What happens if you omit an optional parameter?
_**step defaults to 1; dtype is inferred from input, like defaults to None**_
> - What default value is used?
_**step=1; dtype=None**_

---

## Return Value

What does the function return?

**_ndarray of evenly spaced values_**

## Example

import numpy as np

custom_array = np.arange(
    start=0,
    stop=10,
    step=3,
    dtype=np.int64
)
print(custom_array)


## Expected Output

[0 3 6 9]

## What did you learn about this function?

Write one or two sentences describing something interesting you discovered.

**eager to find out how to apply it**