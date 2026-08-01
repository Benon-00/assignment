# Function 34

## Function Name

```python
math.dist()
```

---

## Purpose

Describe what the function does.

_**Returns the Euclidean distance between two points p & q, given as iterables of coordinates of equal lenght. (in the sense that, the function accepts lists, tuples, or coordinates from a generator, not just rigid coordinate pairs.)**_


## Syntax

```python
math.dist(p, q)
```

---

## Parameters

| Parameter | Required? (Yes/No) | Default Value | Expected Data Type | Description |
|-----------|---------------------|---------------|--------------------|-------------|
| p         | Yes                 | None          | iterable of int/float |First point's coordinates|
| q         | Yes                 | None          | iterable of int/float |Second point's coordinates|


> **Questions to answer**
>
> - Which parameters are required?
_**p & q are required**_
> - Which parameters are optional?
_**None is optional**_
> - What happens if you omit an optional parameter?
_**a TypeError occurs**_
> - What default value is used?
_**None**_

---

## Return Value

What does the function return?

**_float distance_**

## Example

import math

print(math.dist([0,0], [-5,-7]))
print(math.dist([5,8], [-2,4]))


## Expected Output

8.602325267042627
8.06225774829855

## What did you learn about this function?

Write one or two sentences describing something interesting you discovered.

**it is not restricted to a 2d cartesian plane, but takes all points from 2D, 3D, 4D or higher dimensional spaces**