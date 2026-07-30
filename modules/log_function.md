# Function 5

## Function Name

```python
math.log()
```

---

## Purpose

Describe what the function does.

_**Returns the logarithm of x to the given base. If the base is not provided, it returns the natural logarithm (base e)**_

## Syntax

```python
math.log(x, base)
```

---

## Parameters

| Parameter | Required? (Yes/No) | Default Value | Expected Data Type | Description |
|-----------|---------------------|---------------|--------------------|-------------|
| x         | Yes                 | None          | non-negative(positive) int/float|The number to compute the logarithm of |
| base      | No                  | e (Euler's number = 2.71828) | non-negative(positive) int/float | The logarithmic base|

> **Questions to answer**
>
> - Which parameters are required?
_**x is required**_
> - Which parameters are optional?
_**base is optional**_
> - What happens if you omit an optional parameter?
_**The returned value is the natural log (base e)**_
> - What default value is used?
_**base defaults to Euler's number e = 2.718281828**_

---

## Return Value

What does the function return?

**_it returns a float_**

## Example

**__import math_**

**_result1 = round(math.log(100), 2)_**
**_result2 = math.log(100, 10)_**
**_print(result1)__**
**_print(result2)__**


## Expected Output

**_4.61_**
**_2_**

## What did you learn about this function?

Write one or two sentences describing something interesting you discovered.

**_the interesting thing about this function is that the base doesn't have to be ten, it can be any number based on the question being solved**
