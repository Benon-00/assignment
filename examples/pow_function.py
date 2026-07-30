# Function 2

## Function Name

```python
math.pow()
```

---

## Purpose

Describe what the function does.

_**Returns the raised value of x, when raised to the exponent y (x**y), always as a float**_

## Syntax

```python
math.pow(x, y)
```

---

## Parameters

| Parameter | Required? (Yes/No) | Default Value | Expected Data Type | Description |
|-----------|---------------------|---------------|--------------------|-------------|
| x         | Yes                 |  None         |   int or float    | The base number      |
| y         | Yes                 |  None         |   int or float  | The exponent           |

> **Questions to answer**
>
> - Which parameters are required?
_**the required parameter are x & y**_
> - Which parameters are optional?
_**None**_
> - What happens if you omit an optional parameter?
**Ommitting either of the parameters gives a TypeError (which in this case is to say that the function didn't receive both parameters)_**
> - What default value is used?
_**None**_

---

## Return Value

What does the function return?

**_it returns a float_**

## Example

**__import math_**

**_result = math.pow(2, 3)_**
**_print(result)__**

## Expected Output

**_8.0_**

## What did you learn about this function?

Write one or two sentences describing something interesting you discovered.

**_the interesting thing about this function is that the expected results is a float, and not both int/float_**