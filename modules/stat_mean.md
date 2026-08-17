# Function 1

## Function Name

```python
stat.mean()
```

---

## Purpose

Describe what the function does.

_**Calculates the arithmetic mean(average) of numeric data**_


## Syntax

```python
stat.mean(data)
```

---

## Parameters

| Parameter | Required? (Yes/No) | Default Value | Expected Data Type | Description |
|-----------|---------------------|---------------|--------------------|-------------|
| data     | Yes       | None     | iterable of int/float/Decimal/Fraction  |The dataset to average|


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

num1 = [1,2,3]
num2 = [1.4,2.8,3.5]
print(stat.mean(num1))
print(round(stat.mean(num2), 2))


## Expected Output

2
2.57

## What did you learn about this function?

Write one or two sentences describing something interesting you discovered.

**once someone undetsands Numpy, it's easy to understand Statistics**