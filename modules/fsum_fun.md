# Function 35

## Function Name

```python
math.fsum()
```

---

## Purpose

Describe what the function does.

_**Returns an accurate floating-point sum of values in iterable, avoiding precision loss from repeated rounding**_


## Syntax

```python
math.fsum(iterable)
```

---

## Parameters

| Parameter | Required? (Yes/No) | Default Value | Expected Data Type | Description |
|-----------|---------------------|---------------|--------------------|-------------|
|iterable   | Yes                 | None          |iterable int/float  |value to sum |


> **Questions to answer**
>
> - Which parameters are required?
_**the iterable**_
> - Which parameters are optional?
_**None is optional**_
> - What happens if you omit an optional parameter?
_**a TypeError occurs**_
> - What default value is used?
_**None**_

---

## Return Value

What does the function return?

**_float sum_**

## Example

import math

print(math.fsum([0, 0]))
print(math.fsum([5, 8, -2, 24]))
print(math.fsum([-5, -7, -10]))


## Expected Output

0.0
35.0
-22.0

## What did you learn about this function?

Write one or two sentences describing something interesting you discovered.

**the iterbles have to be in list form, otherwise it'll give an error**