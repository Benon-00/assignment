# Function 47

## Function Name

```python
math.sin()
```

---

## Purpose

Describe what the function does.

_**Returns the sine of x radians (where x is in radians)**_


## Syntax

```python
math.sin(x)
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

print(math.sin(0.6754))
print(math.sin(1.543))
print(math.sin(25))


## Expected Output

0.6252095495080406
0.9996137069813006
-0.13235175009777303

## What did you learn about this function?

Write one or two sentences describing something interesting you discovered.

**keen should be considered between degrees and radians; if degrees are used, it has to be converted to radians first using math.radians(degrees)**