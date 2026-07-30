# Function 13

## Function Name

```python
math.fma()
```

---

## Purpose

Describe what the function does.

_**The Fused multiply-add function returns (x * y) + z**_
_**it is computed with precision, followed by a single round to the float format, often providing better accuracy that the direct expression (x * y) + z**_

## Syntax

```python
math.fma(x, y, z)
```

---

## Parameters

| Parameter | Required? (Yes/No) | Default Value | Expected Data Type | Description |
|-----------|---------------------|---------------|--------------------|-------------|
| x         | Yes                 | None          | float             |First number to multiply|
| y         | Yes                 | None          | float             |Second number to multiply|
| z         | Yes                 | None          | float             |third number to add|


> **Questions to answer**
>
> - Which parameters are required?
_**all parameters x, y, z are required**_
> - Which parameters are optional?
_**None is optional, since x, y, z are required parameters**_
> - What happens if you omit an optional parameter?
_**Since x, y, z are the only required parameters, omitting one of them gives a TypeError**_
> - What default value is used?
_**None**_

---

## Return Value

What does the function return?

**_a float_**

## Example

**__import math_**

**_print(math.fma(4, 5, 6))_**
**_print(round(math.fma(4.2, 5.3, 6.4), 2))_**

## Expected Output

**_26.0_**
**_28.66_**


## What did you learn about this function?

Write one or two sentences describing something interesting you discovered.

**_the function only works for python 3.13 and above_**
