# Function 49

## Function Name

```python
math.acosh()
```

---

## Purpose

Describe what the function does.

_**Returns the inverse hyperbolic cosine of x (where x >= 1)**_


## Syntax

```python
math.acosh(x)
```

---

## Parameters

| Parameter | Required? (Yes/No) | Default Value | Expected Data Type | Description |
|-----------|---------------------|---------------|--------------------|-------------|
| x         | Yes                 | None          | int/float(>=1)        |value to compute inverse hyperbolic cosine of|


> **Questions to answer**
>
> - Which parameters are required?
_**x is required**_
> - Which parameters are optional?
_**None is optional**_
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

print(math.acosh(1))
print(math.acosh(1.543))
print(math.acosh(25))


## Expected Output

0.0
0.9999313832829438
3.9116227652145885

## What did you learn about this function?

Write one or two sentences describing something interesting you discovered.

**it's easy to understand**