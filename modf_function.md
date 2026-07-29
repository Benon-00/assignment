# Function 15

## Function Name

```python
math.modf()
```

---

## Purpose

Describe what the function does.

_**Returns the fraction part and integer part of x, both with the same sign as x**_


## Syntax

```python
math.modf(x)
```

---

## Parameters

| Parameter | Required? (Yes/No) | Default Value | Expected Data Type | Description |
|-----------|---------------------|---------------|--------------------|-------------|
| x         | Yes                 | None          | int/float             |Number to split|


> **Questions to answer**
>
> - Which parameters are required?
_**x is required**_
> - Which parameters are optional?
_**None is optional, since x is a required parameters**_
> - What happens if you omit an optional parameter?
_**Since x is the only required parameter, omitting it gives a TypeError**_
> - What default value is used?
_**None**_

---

## Return Value

What does the function return?

**_Tuple (fractional_part, integer_part)_**

## Example

**__import math_**

**_print(math.modf(5))_**
**_print(math.modf(5.2))_**

## Expected Output**_print(math.modf(5))_**

**_(0.0, 5.0)_**
**_0.2, 5.0_**


## What did you learn about this function?

Write one or two sentences describing something interesting you discovered.

**it is a new function learned**