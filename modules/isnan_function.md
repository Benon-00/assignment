# Function 23

## Function Name

```python
math.isnan()
```

---

## Purpose

Describe what the function does.

_**Checks whether x is NaN (Not a Number)**_


## Syntax

```python
math.isnan(x)
```

---

## Parameters

| Parameter | Required? (Yes/No) | Default Value | Expected Data Type | Description |
|-----------|---------------------|---------------|--------------------|-------------|
| x         | Yes                 | None          | int/float          |Value to check|


> **Questions to answer**
>
> - Which parameters are required?
_**x is required**_
> - Which parameters are optional?
_**None is optional, since x is a required parameters**_
> - What happens if you omit an optional parameter?
_**it gives a TypeError, Since x is the only required parameter**_
> - What default value is used?
_**None**_

---

## Return Value

What does the function return?

**_Boolean_**

## Example

**__import math_**

print(math.isnan(5))
print(math.isnan(5.2))
print(math.isnan(-5))
print(math.isnan(float('nan')))


## Expected Output**_print(math.modf(5))_**

False
False
False
True


## What did you learn about this function?

Write one or two sentences describing something interesting you discovered.

**still yet to figure out how to use it**