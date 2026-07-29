# Function 16

## Function Name

```python
math.remainder()
```

---

## Purpose

Describe what the function does.

_**Returns the IEEE 754 style remainder of x with respect to y**_
_**uses x - n*y**_


## Syntax

```python
math.remainder(x, y)
```

---

## Parameters

| Parameter | Required? (Yes/No) | Default Value | Expected Data Type | Description |
|-----------|---------------------|---------------|--------------------|-------------|
| x         | Yes                 | None          | int/float          |Dividend|
| y         | Yes                 | None          | int/float          |Divisor|


> **Questions to answer**
>
> - Which parameters are required?
_**x,y are required**_
> - Which parameters are optional?
_**None is optional, since x,y are both required parameters**_
> - What happens if you omit an optional parameter?
_**Since x, y are the only required parameter, omitting one it gives a TypeError**_
> - What default value is used?
_**None**_

---

## Return Value

What does the function return?

**_Float remainder_**

## Example

**__import math_**

**_print(math.remainder(5, 4))_**
**_print(math.remainder(5.2, 4.2))_**
**_print(math.remainder(-5,-4))_**
**_print(math.remainder(-5.2, 4.2))_**


## Expected Output**_print(math.modf(5))_**

**_(1.0)_**
**_(1.0)_**
**_(-1.0)_**
**_(-1.0)_**


## What did you learn about this function?

Write one or two sentences describing something interesting you discovered.

**it is a new function learned**