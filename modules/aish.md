# Function 50

## Function Name

```python
math.asinh()
```

---

## Purpose

Describe what the function does.

_**Returns the inverse hyperbolic sine of x**_


## Syntax

```python
math.asinh(x)
```

---

## Parameters

| Parameter | Required? (Yes/No) | Default Value | Expected Data Type | Description |
|-----------|---------------------|---------------|--------------------|-------------|
| x         | Yes                 | None          | int/float        |Value to compute inverse hyperbolic sine of|


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

print(math.asinh(0.547))
print(math.asinh(1.543))
print(math.asinh(-25))



## Expected Output

0.5228501361974204
1.218381059342733
-3.9124227656412556

## What did you learn about this function?

Write one or two sentences describing something interesting you discovered.

**unlike acosh(), this one accepts any int/float values**