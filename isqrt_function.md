# Function 7

## Function Name

```python
math.isqrt()
```

---

## Purpose

Describe what the function does.

_**Returns the square root of the non-negative integer n. This is the floor of the exact square root of n, or equivalently the greatest integer a such that a^2 <= n.**_

## Syntax

```python
math.isqrt(n)
```

---

## Parameters

| Parameter | Required? (Yes/No) | Default Value | Expected Data Type | Description |
|-----------|---------------------|---------------|--------------------|-------------|
| n         |Yes                 | None          | non-negative int |The number to compute integer square root of|


> **Questions to answer**
>
> - Which parameters are required?
_**n is required**_
> - Which parameters are optional?
_**None are optional, since n is required**_
> - What happens if you omit an optional parameter?
_**Since existing parameter is required and not optional, omitting the required parameter raises a TypeError if either of the arguments are not intergers, and raises a ValueError if it is negative**_
> - What default value is used?
_**None**_

---

## Return Value

What does the function return?

**_it returns an integer**

## Example

**__import math_**

**_num = math.isqrt(15)_**
**_print(num)__**


## Expected Output

**_3_**


## What did you learn about this function?

Write one or two sentences describing something interesting you discovered.

**the function doesn't round up, but just gives the integer i.e normal sqrt = 3.87298334, but with isqrt = 3**
