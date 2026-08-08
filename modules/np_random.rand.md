# Function 12

## Function Name

```python
np.random.rand()
```

---

## Purpose

Describe what the function does.

_**Generates an array of the given shape, filled with random samples from a uniform distribution over [0, 1]**_


## Syntax

```python
np.random.rand(d0, d1, d2, .... dn)
```

---

## Parameters

| Parameter | Required? (Yes/No) | Default Value | Expected Data Type | Description |
|-----------|---------------------|---------------|--------------------|-------------|
| d0, d1, d2...| No       | None(returns single float)          | int/float  |Dimensions of the returned array|


> **Questions to answer**
>
> - Which parameters are required?
_**None is required**_
> - Which parameters are optional?
_**all arguments are optional**_
> - What happens if you omit an optional parameter?
_**returns a single random float (scalar), not an array**_
> - What default value is used?
_**no explicit default; behaviour changes from scalar to array based on how many dimension args are passed.**_

---

## Return Value

What does the function return?

**_A single float (no args) or an ndarray of the given shape filled with random floats in [0,1]_**

## Example

import numpy as np

np.random.seed(100)
arr = np.random.rand(2, 2)
print(arr)


## Expected Output

[[0.54340494 0.27836939]
 [0.42451759 0.84477613]]

## What did you learn about this function?

Write one or two sentences describing something interesting you discovered.

**eager to find out how to apply it**