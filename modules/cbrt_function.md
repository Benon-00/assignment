# Function 27

## Function Name

```python
math.cbrt()
```

---

## Purpose

Describe what the function does.

_**Returns the cube root of x, both for positive and negative numbers (unlike x**(1/3))**_


## Syntax

```python
math.cbrt(x)
```

---

## Parameters

| Parameter | Required? (Yes/No) | Default Value | Expected Data Type | Description |
|-----------|---------------------|---------------|--------------------|-------------|
| x         | Yes                 | None          | int/float          |Number to cube-root|


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

print(math.cbrt(1))
print(math.cbrt(0))
print(math.cbrt(-5))


## Expected Output**_print(math.modf(5))_**

1.0
0.0
-1.709975946676697


## What did you learn about this function?

Write one or two sentences describing something interesting you discovered.

**it's better off using this as it works for negative numbers, unlike the manual method**