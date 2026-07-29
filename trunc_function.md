# Function 17

## Function Name

```python
math.trunc()
```

---

## Purpose

Describe what the function does.

_**Returns the integer part of x, discarding the fractional part**_
_**it rounds towards 0, meaning that for negative x, it is equivalet to ceil(), and for positive x, it is equivalent to floor()**_
_**if the value is not a float, the result is the raw value of x i.e if x = -5, then the output is -5; if x = 5, then output is 5**_


## Syntax

```python
math.trunc(x)
```

---

## Parameters

| Parameter | Required? (Yes/No) | Default Value | Expected Data Type | Description |
|-----------|---------------------|---------------|--------------------|-------------|
| x         | Yes                 | None          | int/float          |Number to truncate|


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

**_integer_**

## Example

**__import math_**

**_print(math.trunc(5))_**
**_print(math.trunc(5.2))_**
**_print(math.trunc(-5))_**
**_print(math.trunc(-0.2))_**


## Expected Output**_print(math.modf(5))_**

**_(5)_**
**_(5)_**
**_(-5)_**
**_(0)_**


## What did you learn about this function?

Write one or two sentences describing something interesting you discovered.

**the math.trunc() can be used together with math.ceil() & math.floor()**