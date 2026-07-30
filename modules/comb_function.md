# Function 6

## Function Name

```python
math.comb()
```

---

## Purpose

Describe what the function does.

_**Returns the number of ways tho choose k items from n items without repetition and without order**_
_**Evaluates to n! / (k! * (n-k)!) when k <= n and evaluats to zero when k > n**_
_**Also called the binomial coefficient because it is equivalent to the coefficient of k-th term in polynomial exapnsion of (1+x)^n**_
## Syntax

```python
math.comb(n, k)
```

---

## Parameters

| Parameter | Required? (Yes/No) | Default Value | Expected Data Type | Description |
|-----------|---------------------|---------------|--------------------|-------------|
| n         |Yes                 | None          | non-negative int |The number of items|
| k      |Yes                  | None | non-negative int | Number of items to choose|

> **Questions to answer**
>
> - Which parameters are required?
_**both n & k are required**_
> - Which parameters are optional?
_**None are optional, since both n & k are required**_
> - What happens if you omit an optional parameter?
_**Since existing parameters are required and not optional, omitting the required parameters raises a TypeError if either of the arguments are not intergers, and raises a ValueError if they are negative**_
> - What default value is used?
_**None**_

---

## Return Value

What does the function return?

**_it returns an integer: n! / (k! * (n-k)!) when k <= n and evaluats to zero when k > n_**

## Example

**__import math_**

**_comb = math.comb(7,2)_**
**_print(comb)__**


## Expected Output

**_21_**


## What did you learn about this function?

Write one or two sentences describing something interesting you discovered.

**I tried visualizing how i could use this in getting column combinations when doing data analysis, and i realized that the diverse pool combination is when k = n/2 i.e math.comb(10, 5) or math.comb(4, 2), but if i want to get the optimum k without overfitting, then i'll need another method [which i'm eager to find out later]**
