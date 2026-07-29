# Function 3

## Function Name

```python
math.factorial()
```

---

## Purpose

Describe what the function does.

_**Returns the factorial of a non-negative integer (n!) i.e n! = n*(n-1)*(n-2)*(n-3)...**_

## Syntax

```python
math.factorial(n)
```

---

## Parameters

| Parameter | Required? (Yes/No) | Default Value | Expected Data Type | Description |
|-----------|---------------------|---------------|--------------------|-------------|
| n         | Yes                 |  None         |   non-negative int    | The number to compute the factorial of|

> **Questions to answer**
>
> - Which parameters are required?
_**the required parameter is n**_
> - Which parameters are optional?
_**None**_
> - What happens if you omit an optional parameter?
**Since n is the only required parameter, ommitting it gives a TypeError (which in this case is to say that the function didn't receive the parameter n, or got an unexpected parameter)_**
> - What default value is used?
_**None**_

---

## Return Value

What does the function return?

**_it returns an integer_**

## Example

**__import math_**

**_result = math.factorial(4)_**
**_print(result)__**

## Expected Output

**_24.0_**

## What did you learn about this function?

Write one or two sentences describing something interesting you discovered.

**_the interesting thing about this function is that the factorial of 0 is 1 i.e 0! = 1_**
