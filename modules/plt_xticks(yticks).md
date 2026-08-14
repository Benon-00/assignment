# Function 25

## Function Name

```python
plt.xticks()
```

---

## Purpose

Describe what the function does.

_**Gets or sets the tick locations and labels for the x-axis (currently active Axes)**_

## Syntax

```python
plt.xticks(ticks=None, labels=None, **kwargs)
```

---

## Parameters

| Parameter | Required? (Yes/No) | Default Value | Expected Data Type | Description |
|-----------|---------------------|---------------|--------------------|-------------|
|ticks  |No   |current tick locations| array-like | Positions of ticks|
|labels  |No   |str(ticks)| array-like of str| Labels for each tick (must match ticks length if provided)|
|rotation  |No   | 0 | float/str | Rotation angle of labels|
|fontsize |No   | rcParams default| int/str | Label font size |



> **Questions to answer**
>
> - Which parameters are required?
_**none is required; calling plt.xticks() alone returns the current tick locations/labels**_
> - Which parameters are optional?
_**ticks, labels rotation, fontsize**_
> - What happens if you omit an optional parameter?
_**returns the current auto-generated tick positions and defualt numeric labels without changing them**_
> - What default value is used?
_**auto-determined tick locations based on data range (via MaxNLocator), labels are tick values as strings**_

---

## Return Value

What does the function return?

**the tick positions and labeling**

## Example

import matplotlib.pyplot as plt

x= [1, 2, 3]
y= [1, 4, 9]

plt.plot(x, y)
plt.xticks([1,2,3], ['Q1','Q2','Q3'], rotation=45)
plt.show()

## Expected Output
**a line plot with x-axis ticks relabeled as 'Q1','Q2','Q3', each rotated 45 degrees*

## What did you learn about this function?

Write one or two sentences describing something interesting you discovered.

**the plt.xticks/plt.yticks can be used to replace the default x,y values**







