# Function 52

## Function Name

```python
math.cosh()
```

---

## Purpose

Describe what the function does.

_**Returns the hyperbolic cosine of x**_


## Syntax

```python
math.cosh(x)
```

---

## Parameters

| Parameter | Required? (Yes/No) | Default Value | Expected Data Type | Description |
|-----------|---------------------|---------------|--------------------|-------------|
| x         | Yes                 | None          | int/float        |value to compute hyperbolic cosine of|


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

print(math.cosh(0.547))
print(math.cosh(0.9))
print(math.cosh(-0.9))


## Expected Output

1.1533721546712892
1.4330863854487743
1.4330863854487743

## What did you learn about this function?

Write one or two sentences describing something interesting you discovered.

**unlike math.acosh(), this one accepts any range of values**