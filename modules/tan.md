# Function 48

## Function Name

```python
math.tan()
```

---

## Purpose

Describe what the function does.

_**Returns the tangent of x radians (where x is in radians)**_


## Syntax

```python
math.tan(x)
```

---

## Parameters

| Parameter | Required? (Yes/No) | Default Value | Expected Data Type | Description |
|-----------|---------------------|---------------|--------------------|-------------|
| x         | Yes                 | None          | int/float        |Angle in radians|


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

print(math.tan(0.6754))
print(math.tan(1.543))
print(math.tan(25))


## Expected Output

0.8010814250872392
35.96671059629233
-0.13352640702153587

## What did you learn about this function?

Write one or two sentences describing something interesting you discovered.

**keen should be considered between degrees and radians; if degrees are used, it has to be converted to radians first utang math.radians(degrees)**