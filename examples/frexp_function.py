# Function 19

## Function Name

```python
math.frexp()
```

---

## Purpose

Describe what the function does.

_**Decomposes x into a mantissa m and exponent e, such that x = m * 2**e**_


## Syntax

```python
math.frexp(x)
```

---

## Parameters

| Parameter | Required? (Yes/No) | Default Value | Expected Data Type | Description |
|-----------|---------------------|---------------|--------------------|-------------|
| x         | Yes                 | None          | int/float          |Number to decompose|


> **Questions to answer**
>
> - Which parameters are required?
_**x is required**_
> - Which parameters are optional?
_**None is optional, since x is a required parameter**_
> - What happens if you omit an optional parameter?
_**it gives a TypeError, Since x is the only required parameter**_
> - What default value is used?
_**None**_

---

## Return Value

What does the function return?

**_a Tuple (mantissa as float, exponent as integer)_**

## Example

**__import math_**

**_print(math.frexp(5))_**
**_print(math.frexp(5.2))_**
**_print(math.frexp(-5))_**


## Expected Output

(0.625, 3)
(0.65, 3)
(-0.625, 3)


## What did you learn about this function?

Write one or two sentences describing something interesting you discovered.

**it takes in both int/float, then the output is (float, integer)**