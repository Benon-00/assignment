# Function 14

## Function Name

```python
math.fmod()
```

---

## Purpose

Describe what the function does.

_**Returns the floating-point remainder of x/y, resuts having the sign of x**_
_**it is computed with precision, often providing better accuracy that the expression x % y**_

## Syntax

```python
math.fmod(x, y)
```

---

## Parameters

| Parameter | Required? (Yes/No) | Default Value | Expected Data Type | Description |
|-----------|---------------------|---------------|--------------------|-------------|
| x         | Yes                 | None          | int/float             |Dividend|
| y         | Yes                 | None          | int/float             |Divisor|


> **Questions to answer**
>
> - Which parameters are required?
_**all parameters x, y are required**_
> - Which parameters are optional?
_**None is optional, since x, y are required parameters**_
> - What happens if you omit an optional parameter?
_**Since x, y are the only required parameters, omitting one of them gives a TypeError**_
> - What default value is used?
_**None**_

---

## Return Value

What does the function return?

**_a float remainder_**

## Example

**__import math_**

**_print(math.fmod(5, 4))_**
**_print(round(math.fmod(5.2, 4.3), 2))_**

## Expected Output

**_1.0_**
**_0.9_**


## What did you learn about this function?

Write one or two sentences describing something interesting you discovered.

**if x > y, then the remainder is the x**
