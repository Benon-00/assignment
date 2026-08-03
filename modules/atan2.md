# Function 45

## Function Name

```python
math.atan2()
```

---

## Purpose

Describe what the function does.

_**Returns atan(y/x), in radians, using the signs of both arguments to determine the correct quadrant**_


## Syntax

```python
math.atan2(y, x)
```

---

## Parameters

| Parameter | Required? (Yes/No) | Default Value | Expected Data Type | Description |
|-----------|---------------------|---------------|--------------------|-------------|
| y         | Yes                 | None          | int/float        |Y-coordinate   |
| x         | Yes                 | None          | int/float        |X-coordinate |


> **Questions to answer**
>
> - Which parameters are required?
_**x, y are required**_
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

print(math.atan2(-10, 5))
print(math.atan2(0, 0))
print(math.atan2(50, 21))
print(math.atan2(-40,-10))


## Expected Output

-1.1071487177940904
0.0
1.1731683352727673
-1.8157749899217608

## What did you learn about this function?

Write one or two sentences describing something interesting you discovered.

**the idea of using the sign of both arguments to get the quadrant is a good one!**