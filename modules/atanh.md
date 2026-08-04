# Function 51

## Function Name

```python
math.atanh()
```

---

## Purpose

Describe what the function does.

_**Returns the inverse hyperbolic function of x (where -1< X < 1)**_


## Syntax

```python
math.atanh(x)
```

---

## Parameters

| Parameter | Required? (Yes/No) | Default Value | Expected Data Type | Description |
|-----------|---------------------|---------------|--------------------|-------------|
| x         | Yes                 | None          | float( -1< X < 1)  |Value to compute inverse hyperbolic tangent of|


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

print(math.atanh(0.547))
print(math.atanh(0.9))
print(math.atanh(-0.9))


## Expected Output

0.6140903625450161
1.4722194895832204
-1.4722194895832204

## What did you learn about this function?

Write one or two sentences describing something interesting you discovered.

**it only accepts values in a strict bracket of between -1 to 1 (-1 & 1 not included)**