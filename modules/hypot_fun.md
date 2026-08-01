# Function 36

## Function Name

```python
math.hypot()
```

---

## Purpose

Describe what the function does.

_**Returns the Euclidean norm, sqrt(sum(x**2 for x in coordinates)), generalizing the 2D hypotenuse formula to any number of dimensions**_


## Syntax

```python
math.hypot(*coordinates)
```

---

## Parameters

| Parameter | Required? (Yes/No) | Default Value | Expected Data Type | Description |
|-----------|---------------------|---------------|--------------------|-------------|
|*coordinates   | No    |Returns 0.0 if none given  | int/float(variadic) |Coordinates value|


> **Questions to answer**
>
> - Which parameters are required?
_**None strictly**_
> - Which parameters are optional?
_**All arguments are optional**_
> - What happens if you omit an optional parameter?
_**Returns 0.0**_
> - What default value is used?
_**0.0 is the default value**_

---

## Return Value

What does the function return?

**_float_**

## Example

import math

print(math.hypot(0, 0))
print(math.hypot(5, 8, -2, 24))
print(math.hypot(-5, -7, -10))


## Expected Output**_print(math.modf(5))_**

0.0
25.865034312755125
13.19090595827292

## What did you learn about this function?

Write one or two sentences describing something interesting you discovered.

**nornally, it's easier to visualize the hypotensue of a 2D case. Beyond that, the complexity of the hypotenuse increases**