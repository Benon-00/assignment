# Function 26

## Function Name

```python
math.ulp()
```

---

## Purpose

Describe what the function does.

_**Returns the value of the least siginificant bit of x (the size of the gap between x and the nearest representable float)**_


## Syntax

```python
math.ulp(x)
```

---

## Parameters

| Parameter | Required? (Yes/No) | Default Value | Expected Data Type | Description |
|-----------|---------------------|---------------|--------------------|-------------|
| x         | Yes                 | None          | int/float          |Value to inspect|



> **Questions to answer**
>
> - Which parameters are required?
_**x is required**_
> - Which parameters are optional?
_**None is optional, since x is the only required argument**_
> - What happens if you omit an optional parameter?
_**a TypeError occurs**_
> - What default value is used?
_**None**_

---

## Return Value

What does the function return?

**_float_**

## Example

import math

print(math.ulp(1))
print(math.ulp(0))
print(math.ulp(-5))


## Expected Output**_print(math.modf(5))_**

2.220446049250313e-16
5e-324
8.881784197001252e-16

## What did you learn about this function?

Write one or two sentences describing something interesting you discovered.

**yet to figure out how to apply this**