# Function 31

## Function Name

```python
math.log1p()
```

---

## Purpose

Describe what the function does.

_**Returns the natural logarithm of 1+x, accurate even for every small x**_


## Syntax

```python
math.log1p(x)
```

---

## Parameters

| Parameter | Required? (Yes/No) | Default Value | Expected Data Type | Description |
|-----------|---------------------|---------------|--------------------|-------------|
| x         | Yes                 | None          | int/float(>-1)     |Value used in 1+x|


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

print(math.log1p(1))
print(math.log1p(0))
print(math.log1p(4))


## Expected Output**_print(math.modf(5))_**

0.6931471805599453
0.0
1.6094379124341003

## What did you learn about this function?

Write one or two sentences describing something interesting you discovered.

**it's true that it gives an error for anything <=-1**