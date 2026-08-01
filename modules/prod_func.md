# Function 37

## Function Name

```python
math.prod()
```

---

## Purpose

Describe what the function does.

_**Returns the product of all elements in iterable, multiplied by an optional start value**_


## Syntax

```python
math.prod(iterable, *, start-=1)
```

---

## Parameters

| Parameter | Required? (Yes/No) | Default Value | Expected Data Type | Description |
|-----------|---------------------|---------------|--------------------|-------------|
| iterable  | Yes                 | None          |iterable int/float  |Value to multiply|
| start     | No                 | 1          |int/float  |Initial value to multiply from|


> **Questions to answer**
>
> - Which parameters are required?
_**iterable**_
> - Which parameters are optional?
_**start**_
> - What happens if you omit an optional parameter?
_**uses the deafult 1 as the stating multiplier**_
> - What default value is used?
_**start=1**_

---

## Return Value

What does the function return?

**_int/float product_**

## Example

import math

print(math.prod([0]))
print(math.prod([5, 8, -2, 24]))
print(math.prod([-5, -7, -10]))


## Expected Output**_print(math.modf(5))_**

0
-1920
-350

## What did you learn about this function?

Write one or two sentences describing something interesting you discovered.

**the product of either int or float dependes on the input**