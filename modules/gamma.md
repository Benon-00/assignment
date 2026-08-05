# Function 57

## Function Name

```python
math.gamma()
```

---

## Purpose

Describe what the function does.

_**Returns the gamma function at x, a generalization of factorial to real (and complex) numbers, where gamma(n) = (n-1)!**_


## Syntax

```python
math.gamma(x)
```

---

## Parameters

| Parameter | Required? (Yes/No) | Default Value | Expected Data Type | Description |
|-----------|---------------------|---------------|--------------------|-------------|
| x         | Yes                 | None          | non-negative int/float(>0) |value to evaluate|


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

print(math.gamma(0.547))
print(math.gamma(10))
print(math.gamma(1))


## Expected Output

1.6245936051926158
362880.0
1.0

## What did you learn about this function?

Write one or two sentences describing something interesting you discovered.

**researching more on it**