# Function 24

## Function Name

```python
math.ldexp()
```

---

## Purpose

Describe what the function does.

_**Returns x * (2**i), the inverse operation of math.frexp()**_

## Syntax

```python
math.ldexp(x, i)
```

---

## Parameters

| Parameter | Required? (Yes/No) | Default Value | Expected Data Type | Description |
|-----------|---------------------|---------------|--------------------|-------------|
| x         | Yes                 | None          | float              |Mantissa     |
| i         | Yes                 | None          | int                |Exponent     |


> **Questions to answer**
>
> - Which parameters are required?
_**x, i are required**_
> - Which parameters are optional?
_**None is optional, since x,i are both required parameters**_
> - What happens if you omit an optional parameter?
_**it gives a TypeError, Since x, i are the only required parameters**_
> - What default value is used?
_**None**_

---

## Return Value

What does the function return?

**_Float_**

## Example

**__import math_**

print(math.ldexp(0.5, 4))


## Expected Output**_print(math.modf(5))_**

8


## What did you learn about this function?

Write one or two sentences describing something interesting you discovered.

**the math.frexp() & math.ldexp() can be used to check validity oof something**