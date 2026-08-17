# Function 2

## Function Name

```python
stat.median()
```

---

## Purpose

Describe what the function does.

_**Calculates the arithmetic median(nidle value) of numeric data**_
_**For a even number of data points, it returns the average of the two middle values**_

## Syntax

```python
stat.median(data)
```

---

## Parameters

| Parameter | Required? (Yes/No) | Default Value | Expected Data Type | Description |
|-----------|---------------------|---------------|--------------------|-------------|
| data     | Yes       | None     | iterable of int/float/Decimal/Fraction  |The dataset to find the median of|


> **Questions to answer**
>
> - Which parameters are required?
_**data is required**_
> - Which parameters are optional?
_**None is optional**_
> - What happens if you omit an optional parameter?
_**Since there are no optional parameters, omitting the required data gives a StatisticseError**_
> - What default value is used?
_**None**_

---

## Return Value

What does the function return?

**int/float: inferred from the input**

## Example

import statistics as stat

num1 = [1,2,3,4]
num2 = [1.4,2.8,3.5, 4.7]
print(stat.median(num1))
print(round(stat.median(num2), 2))


## Expected Output
2.5
3.15

## What did you learn about this function?

Write one or two sentences describing something interesting you discovered.

**once someone undetsands Numpy, it's easy to understand Statistics**