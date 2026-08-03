# Function 44

## Function Name

```python
math.atan()
```

---

## Purpose

Describe what the function does.

_**Returns the arc tangent of x, in radians**_


## Syntax

```python
math.atan(x)
```

---

## Parameters

| Parameter | Required? (Yes/No) | Default Value | Expected Data Type | Description |
|-----------|---------------------|---------------|--------------------|-------------|
| x         | Yes                 | None          | int/float        |Value to compute arc tangent of|


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

**_float radians_**

## Example

import math

print(math.atan(-1))
print(math.atan(0))
print(math.atan(50))
print(math.atan(1))


## Expected Output

-0.7853981633974483
0.0
1.550798992821746
0.7853981633974483

## What did you learn about this function?

Write one or two sentences describing something interesting you discovered.

**the atan() accepts numbers beyond the [-1,1] range**