# Function 54

## Function Name

```python
math.tanh()
```

---

## Purpose

Describe what the function does.

_**Returns the hyperbolic tangent of x**_


## Syntax

```python
math.tanh(x)
```

---

## Parameters

| Parameter | Required? (Yes/No) | Default Value | Expected Data Type | Description |
|-----------|---------------------|---------------|--------------------|-------------|
| x         | Yes                 | None          | int/float        |value to compute hyperbolic tangent of|


> **Questions to answer**
>
> - Which parameters are required?
_**x is required**_
> - Which parameters are optional?
_**None is optional**_
> - What happens if you omit an optional parameter?
_**a TypeError occurs**_
> - What default value is used?
_**None**_

---

## Return Value

What does the function return?

**_float_**

## Example

import math

print(math.tanh(0.547))
print(math.tanh(10))
print(math.tanh(-10))


## Expected Output

0.4982683981572956
0.9999999958776927
-0.9999999958776927
## What did you learn about this function?

Write one or two sentences describing something interesting you discovered.

**comapred to sinh & cosh, tanh gives very small values**