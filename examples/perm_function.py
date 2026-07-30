# Function 9

## Function Name

```python
math.perm()
```

---

## Purpose

Describe what the function does.

_**Returns the number of ways tho choose k items from n items without repetition and with order**_
_**Evaluates to n! / (k! * (n-k)!) when k <= n and evaluats to zero when k > n**_
_**if k is not specified or is None, then k defaults to n and the function returns n! i.e k=n, hence math.perm(n, k=n)**_
## Syntax

```python
math.perm(n, k=None)
```

---

## Parameters

| Parameter | Required? (Yes/No) | Default Value | Expected Data Type | Description |
|-----------|---------------------|---------------|--------------------|-------------|
| n         |Yes                 | None          | non-negative int |The totalnumber of items|
| k      |Yes                  | n | non-negative int | Number of items to choose and arrange|

> **Questions to answer**
>
> - Which parameters are required?
_**n is required**_
> - Which parameters are optional?
_**k is optional**_
> - What happens if you omit an optional parameter?
_**if k is omitted, then k defaults to n [k=n]**_
> - What default value is used?
_**k=n**_

---

## Return Value

What does the function return?

**_it returns an integer: n! / (k! * (n-k)!) when k <= n and evaluats to zero when k > n_**

## Example

**__import math_**

**_comb = math.perm(5)_**
**_comb2 = math.perm(5, 5)_**
**_comb3 = math.perm(5, 2)_**
**_print(comb, comb2, comb3)__**


## Expected Output

**_120, 120, 20_**


## What did you learn about this function?

Write one or two sentences describing something interesting you discovered.

**it's similar to math.comb(), but the values are arranges**