# Function 20

## Function Name

```python
math.isclose()
```

---

## Purpose

Describe what the function does.

_**Checks whether two values a & b are approximately equal, within a given tolerance, and retuns True or False**_


## Syntax

```python
math.isclose(a, b, *, rel_tol=1e-09, abs_tol=0.0)
```

---

## Parameters

| Parameter | Required? (Yes/No) | Default Value | Expected Data Type | Description |
|-----------|---------------------|---------------|--------------------|-------------|
| a         | Yes                 | None          | int/float          |First Value|
| b         | Yes                 | None          | int/float          |Second Value|
| rel_tol   | No                  |1e-09          | float              |Relative Tolerance|
|abs_tol    | No                  |0.0            | float              |Absolute Tolerance|


> **Questions to answer**
>
> - Which parameters are required?
_**a,b are required**_
> - Which parameters are optional?
_**rel_tol, abs_tol**_
> - What happens if you omit an optional parameter?
_**uses default tolerance**_
> - What default value is used?
_**rel_tol=1e-09; abs_tol=0.0**_

---

## Return Value

What does the function return?

**_True or False_**

## Example

**__import math_**

print(math.isclose(5, 6))
print(math.isclose(5.2, 0))
print(math.isclose(-5, -25))
print(math.isclose(1.000000001, 1.0))


## Expected Output

False
False
False
False


## What did you learn about this function?

Write one or two sentences describing something interesting you discovered.

**I am yet to think of how to use this**