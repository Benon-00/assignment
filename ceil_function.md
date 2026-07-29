# Function 10

## Function Name

```python
math.ceil()
```

---

## Purpose

Describe what the function does.

_**Returns the smallest integer greater or equal to x (the ceiling of x)**_
_**if x is not a float, delegates to x._ceil_, which should return an integral value**_

## Syntax

```python
math.ceil(x)
```

---

## Parameters

| Parameter | Required? (Yes/No) | Default Value | Expected Data Type | Description |
|-----------|---------------------|---------------|--------------------|-------------|
| x         | Yes                 | None          | int/float|The number to round up|


> **Questions to answer**
>
> - Which parameters are required?
_**x is required**_
> - Which parameters are optional?
_**None is optional, since x is the only required parameter**_
> - What happens if you omit an optional parameter?
_**Since x is the only required parameter, omitting it gives a TypeError**_
> - What default value is used?
_**None**_

---

## Return Value

What does the function return?

**_an integer_**

## Example

**__import math_**

**_print(math.ceil(4.5))_**


## Expected Output

**_5_**


## What did you learn about this function?

Write one or two sentences describing something interesting you discovered.

**_the function rounds to the nearest whole number i.e if it's a float, it rounds up to the nearest whole number i.e math.ceil(4.2) will give 5; if it's an integer, the outcome is the same as the input value i.e math.ceil(5) will give 5_**