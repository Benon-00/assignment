# Function 38

## Function Name

```python
math.sumprod()
```

---

## Purpose

Describe what the function does.

_**Returns the sum of products of corresponding elements from two iterables p & q, computed with extra precision**_


## Syntax

```python
math.sumprod(p, q)
```

---

## Parameters

| Parameter | Required? (Yes/No) | Default Value | Expected Data Type | Description |
|-----------|---------------------|---------------|--------------------|-------------|
| p         | Yes                 | None          | iterable int/float |First sequence|
| q         | Yes                 | None          | iterable int/float |Second sequence|

> **Questions to answer**
>
> - Which parameters are required?
_**p & q are required**_
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

print(math.sumprod([0], [5]))
print(math.sumprod([5, 8], [-2, 24]))


## Expected Output**_print(math.modf(5))_**

0
182

## What did you learn about this function?

Write one or two sentences describing something interesting you discovered.

**in this case, an argument is equal to 1 list, meaning two lists are required**