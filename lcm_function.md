# Function 8

## Function Name

```python
math.lcm()
```

---

## Purpose

Describe what the function does.

_**Returns the least common multiple of the specified interger arguments.**_
_**If all arguments are non-zero, then the returned value is the smallest positive integer that is a multiple of all arguments.**_
_**If any of the arguments is zero, then the returned value is 0, and if there are no arguments, it returns 1**_



## Syntax

```python
math.lcm(*integers)
```

---

## Parameters

| Parameter | Required? (Yes/No) | Default Value | Expected Data Type | Description |
|-----------|---------------------|---------------|--------------------|-------------|
|*integers  |No                 |Returns 1 if none is given          |int(varies) |The number to find LCM of|


> **Questions to answer**
>
> - Which parameters are required?
_**None is strictly required, since the range is: no paramaters---*integers*_
> - Which parameters are optional?
_**All are optional**_
> - What happens if you omit an optional parameter?
_**the returned value becomes 1, when no parameters are given_
> - What default value is used?
_**the default value is 1**_

---

## Return Value

What does the function return?

**_it returns an integer**

## Example

**__import math_**

**_num = math.lcm(20,75)_**
**_print(num)__**


## Expected Output

**_300_**


## What did you learn about this function?

Write one or two sentences describing something interesting you discovered.

**the function is easy to understand and use**