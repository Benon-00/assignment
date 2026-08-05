# Function 58

## Function Name

```python
math.lgamma()
```

---

## Purpose

Describe what the function does.

_**Returns the natural logarithm of the absoute value of the Gamma function at x, useful for avoiding overfow with large factorial-like calculations**_


## Syntax

```python
math.lgamma(x)
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

print(math.lgamma(0.547))
print(math.lgamma(10))
print(math.lgamma(1))


## Expected Output

0.48525769539196767
12.801827480081467
0.0

## What did you learn about this function?

Write one or two sentences describing something interesting you discovered.

**researching more on it**