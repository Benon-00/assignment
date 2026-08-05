# Function 56

## Function Name

```python
math.erfc()
```

---

## Purpose

Describe what the function does.

_**Returns the complementary error function of x, computed as 1- erf(x), but with better precision for large x**_


## Syntax

```python
math.erfc(x)
```

---

## Parameters

| Parameter | Required? (Yes/No) | Default Value | Expected Data Type | Description |
|-----------|---------------------|---------------|--------------------|-------------|
| x         | Yes                 | None          | int/float        |value to evaluate|


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

print(math.erfc(0.547))
print(math.erfc(10))
print(math.erfc(-10))


## Expected Output

0.4391822681290505
2.088487583762545e-45
2.0

## What did you learn about this function?

Write one or two sentences describing something interesting you discovered.

**researching more on it on where it is utilized**