# Function 4

## Function Name

```python
stat.stdev()
```

---

## Purpose

Describe what the function does.

_**Calculates the sample standard deviation, a measure of the spread/dipsersion of the sample data from a larger population (divides by n-1)**_

## Syntax

```python
stat.stdev(data, xbar=None)
```

---

## Parameters

| Parameter | Required? (Yes/No) | Default Value | Expected Data Type | Description |
|-----------|---------------------|---------------|--------------------|-------------|
| data     | Yes       | None     | iterable of int/float/Decimal/Fraction (must have at least 2 data points)  |The sample dataset|
| xbar(mean)    | No       | None(mean is autocomputed)     | float |Precomputed mean of data, to save recomputation|




> **Questions to answer**
>
> - Which parameters are required?
_**data is required, and must contain at least 2 data points**_
> - Which parameters are optional?
_**xbar is optional**_
> - What happens if you omit an optional parameter?
_**if xbar is omitted, stdev() automatically calculates the mean of data internally before computing the standard deviation**_
> - What default value is used?
_**xbar=None, which signals the function to compute the mean itself**_

---

## Return Value

What does the function return?

**the smaple stdev as a float (or matching numeric type of input)**

## Example

import statistics as stat

data = [2,4,4,4,5,5,7,9]
print(round(stat.stdev(data), 2))


## Expected Output
2.14

## What did you learn about this function?

Write one or two sentences describing something interesting you discovered.

**once someone undetsands Numpy, it's easy to understand Statistics**