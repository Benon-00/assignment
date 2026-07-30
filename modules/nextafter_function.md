# Function 25

## Function Name

```python
math.nextafter()
```

---

## Purpose

Describe what the function does.

_**Returns the floating-point value _steps_ steps after x, in the direction of y**_


## Syntax

```python
math.nextafter(x, y, steps=1)
```

---

## Parameters

| Parameter | Required? (Yes/No) | Default Value | Expected Data Type | Description |
|-----------|---------------------|---------------|--------------------|-------------|
| x         | Yes                 | None          | int/float          |Starting value|
| y         | Yes                 | None          | int/float          |Direction target|
| steps         | No               | 1          | int          |Number of steps to take|


> **Questions to answer**
>
> - Which parameters are required?
_**x, y are both required**_
> - Which parameters are optional?
_**_steps_ is optional**_
> - What happens if you omit an optional parameter?
_**it uses the default value of 1 _steps_ towards y**_
> - What default value is used?
_**_steps_=1**_

---

## Return Value

What does the function return?

**_float_**

## Example

**__import math_**

print(math.nextafter(1, 2))
print(math.nextafter(3, 8))
print(math.nextafter(0, -5))


## Expected Output**_print(math.modf(5))_**

1.0000000000000002
3.0000000000000004
-5e-324


## What did you learn about this function?

Write one or two sentences describing something interesting you discovered.

**yet to figure out how to apply this**