# Function 12

## Function Name

```python
math.floor()
```

---

## Purpose

Describe what the function does.

_**Returns the largest integer less than or equal to x (the floor of x)**_
_**if x is not a float, delegates to x._floor_, which should return an integral value**_

## Syntax

```python
math.floor(x)
```

---

## Parameters

| Parameter | Required? (Yes/No) | Default Value | Expected Data Type | Description |
|-----------|---------------------|---------------|--------------------|-------------|
| x         | Yes                 | None          | int/float|The number to round down|


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

**_print(math.floor(4.5))_**


## Expected Output

**_4_**


## What did you learn about this function?

Write one or two sentences describing something interesting you discovered.

**_the function rounds down to the nearest whole number i.e if it's a float, it rounds down to the nearest whole number i.e math.ceil(4.2) will give 4; if it's an integer, the outcome is the same as the input value i.e math.ceil(5) will give 5_**
