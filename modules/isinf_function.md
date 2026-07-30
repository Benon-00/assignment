# Function 22

## Function Name

```python
math.isinf()
```

---

## Purpose

Describe what the function does.

_**Checks whether x is positive or negative infinity**_


## Syntax

```python
math.isinf(x)
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
_**None is optional, since x is a required parameter**_
> - What happens if you omit an optional parameter?
_**it gives a TypeError, Since x is the only required parameter**_
> - What default value is used?
_**None**_

---

## Return Value

What does the function return?

**_integer_**

## Example

**__import math_**

print(math.isinf(5))
print(math.isinf(5.2))
print(math.isinf(-5))
print(math.isinf(1.000000001e309))


## Expected Output

False
False
False
True


## What did you learn about this function?

Write one or two sentences describing something interesting you discovered.

**it'll be rare to find an instance to get the outcome as True, unless in scientific calculations**