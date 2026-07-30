# Function 18

## Function Name

```python
math.copysign()
```

---

## Purpose

Describe what the function does.

_**Returns the absolute value of x, but with the sign of y**_


## Syntax

```python
math.copysign(x, y)
```

---

## Parameters

| Parameter | Required? (Yes/No) | Default Value | Expected Data Type | Description |
|-----------|---------------------|---------------|--------------------|-------------|
| x         | Yes                 | None          | int/float          |Number to take value from|
| y         | Yes                 | None          | int/float          |Number to take sign from|


> **Questions to answer**
>
> - Which parameters are required?
_**Both x, y are required**_
> - Which parameters are optional?
_**None is optional, since both x, y are required parameters**_
> - What happens if you omit an optional parameter?
_**a TypeError occurs, Since both x,y are the only required parameter**_
> - What default value is used?
_**None**_

---

## Return Value

What does the function return?

**_float_**

## Example

**__import math_**

**_print(math.trunc(5))_**
**_print(math.trunc(5.2, -4.3))_**
**_print(math.trunc(-5, 3))_**


## Expected Output

**_TypeError_**
**_-5.2_**
**_(3)_**


## What did you learn about this function?

Write one or two sentences describing something interesting you discovered.

**it takes both int/float, but the results is a float**