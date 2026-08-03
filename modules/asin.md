# Function 43

## Function Name

```python
math.asin()
```

---

## Purpose

Describe what the function does.

_**Returns the arc sine of x, in radians, for x in range [-1,1]**_


## Syntax

```python
math.asin(x)
```

---

## Parameters

| Parameter | Required? (Yes/No) | Default Value | Expected Data Type | Description |
|-----------|---------------------|---------------|--------------------|-------------|
| x         | Yes                 | None          | int/float (-1,1)        |Value to compute arc sine of|


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

print(math.asin(-1))
print(math.asin(0))
print(math.asin(0.6754))
print(math.asin(1))


## Expected Output

-1.5707963267948966
0.0
0.7415069760599595
1.5707963267948966

## What did you learn about this function?

Write one or two sentences describing something interesting you discovered.

**for this case, asin(0)=0, compared to acos(0)=1.571**