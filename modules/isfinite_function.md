# Function 21

## Function Name

```python
math.isfinite()
```

---

## Purpose

Describe what the function does.

_**Checks whether x is neither infinite nor NaN**_


## Syntax

```python
math.isfinite(x)
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

**_Boolean True or False_**

## Example

**__import math_**

print(math.isfinite(5))
print(math.isfinite(5.2))
print(math.isfinite(-5))
print(math.isfinite(1.000000001))


## Expected Output**_print(math.modf(5))_**

True
True
True
True


## What did you learn about this function?

Write one or two sentences describing something interesting you discovered.

**interesting thing is that, its purpose it to make sure the argument x is not infinite or NaN**