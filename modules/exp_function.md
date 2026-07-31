# Function 28

## Function Name

```python
math.exp()
```

---

## Purpose

Describe what the function does.

_**Returns e raised to power x**_


## Syntax

```python
math.exp(x)
```

---

## Parameters

| Parameter | Required? (Yes/No) | Default Value | Expected Data Type | Description |
|-----------|---------------------|---------------|--------------------|-------------|
| x         | Yes                 | None          | int/float          |Exponent     |


> **Questions to answer**
>
> - Which parameters are required?
_**x is required**_
> - Which parameters are optional?
_**None is optional, since x is the only required parameter**_
> - What happens if you omit an optional parameter?
_**a TypeError occurs**_
> - What default value is used?
_**None**_

---

## Return Value

What does the function return?

**_float_**

## Example

**__import math_**

print(math.exp(1))
print(math.exp(0))
print(math.exp(-5))


## Expected Output**_print(math.modf(5))_**

2.718281828459045
1.0
0.006737946999085467

## What did you learn about this function?

Write one or two sentences describing something interesting you discovered.

**easy to understand, but I wonder if it has a working relation with math.frexp(); i will found out.**