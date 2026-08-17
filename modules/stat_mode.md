# Function 3

## Function Name

```python
stat.mode()
```

---

## Purpose

Describe what the function does.

_**Returns the single most common data point(the mode) from a dataset**_
_**Works with numeric and non-numeric data (e.g string)**_

## Syntax

```python
stat.mode(data)
```

---

## Parameters

| Parameter | Required? (Yes/No) | Default Value | Expected Data Type | Description |
|-----------|---------------------|---------------|--------------------|-------------|
| data     | Yes       | None     | iterable of int/float/Decimal/Fraction/Strings  |The dataset to find the mode of|


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

**the most frequently occurring value in the dataset, in its original data type(e.g int, str)**

## Example

import statistics as stat

data = ['red', 'blue', 'blue', 'green', 'blue']
print(stat.mode(data))


## Expected Output
blue

## What did you learn about this function?

Write one or two sentences describing something interesting you discovered.

**once someone undetsands Numpy, it's easy to understand Statistics**