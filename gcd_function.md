# Function 4

## Function Name

```python
math.gcd()
```

---

## Purpose

Describe what the function does.

_**Returns the greatest common divisor of the given interger(s)**_

## Syntax

```python
math.gcd(*integers)
```

---

## Parameters

| Parameter | Required? (Yes/No) | Default Value | Expected Data Type | Description |
|-----------|---------------------|---------------|--------------------|-------------|
| *integers | No, because one can leave it blank | Returns 0 if called with no arguments | int(one or more)    | The integersto find GCD of|

> **Questions to answer**
>
> - Which parameters are required?
_**at least 2 integers to give meaningful GCD**_
> - Which parameters are optional?
_*  All of them essentially, because you can pass zero, one or many integers**_
> - What happens if you omit an optional parameter?
_**The returned value defaults to 0 if no argument(s) are passed**_
> - What default value is used?
_*  0**_

---

## Return Value

What does the function return?

**_it returns a positive integer_**

## Example

**__import math_**

**_result = math.gcd(48, 60, 18)_**
**_print(result)__**

or 
**_result2 = math.gcd(-48, -60, -18)_** #since these are negative numbers, their absolute value |integer| are used to get the GCD
**_print(result2)__**

## Expected Output

**_6_**

## What did you learn about this function?

Write one or two sentences describing something interesting you discovered.

**_the interesting thing about this function is that even for negative integers, the absolute value is used to get the answer_**