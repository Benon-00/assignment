# Function 1

## Function Name

```python
plt.plot()
```

---

## Purpose

Describe what the function does.

_**Draws lines and/or markers connecting a series of data points; the core function for line/scatter stylecharts**_


## Syntax

```python
matplotlib.pyplot.plot(*args, scalex=True, scaley=True, data=None, **kwargs)
```

---

## Parameters

| Parameter | Required? (Yes/No) | Default Value | Expected Data Type | Description |
|-----------|---------------------|---------------|--------------------|-------------|
| x     | No                 | range(len(y))      | array-like         |X-cordinates of points|
| y     | yes                | None      | array-like         |Y-cordinates of points|
| fmt   | No                 | '-'(solid line)    | str       | Format string e.g 'ro' for red circles|
| color     | No             | next in cylce      | str         |Line/marker color|
| linewidth | No             | 1.5      | float         |Width of the line|
| linestyle | No             | '-'     | str         |Linestyle (--, -, :)|
| marker    | No             | None      | str         | Marker style ('o' 'x', 's')|
| label     | No             | None      | str         |Label for legend|

> **Questions to answer**
>
> - Which parameters are required?
_**y is required* (x is optional; if only one array is given, it's treated as y)*_
> - Which parameters are optional?
_**everything else is optional**_
> - What happens if you omit an optional parameter?
_**matplotlib uses defaults; solidline, autocolor cycling, no markers, no legend label**_
> - What default value is used?
_**solid line style; next color in current color cylce; linewidth of 1.5; No marker, No label**_

---

## Return Value

What does the function return?

**a 2d plot**

## Example

import matplotlib.pyplot as plt

x = (1, 2 ,3)
y = [2.5, 3.4, 4.5]

plt.plot(x, y,
         c='red', lw=2, label='first line', ls='--', marker='o', mec='green', mfc='black')
plt.show()
plt.legend()


## Expected Output

a 2d plot

## What did you learn about this function?

Write one or two sentences describing something interesting you discovered.

**it's fun playing around with the arguments**