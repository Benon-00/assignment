# Function 2

## Function Name

```python
plt.scatter()
```

---

## Purpose

Describe what the function does.

_**Creates a scatter plot of x vs y; useful for showing individual data points without connecting lines**_


## Syntax

```python
matplotlib.pyplot.scatter(x, y, s=None, c=None, marker=None, cmpa=None, alpha=None, *kwargs)
```

---

## Parameters

| Parameter | Required? (Yes/No) | Default Value | Expected Data Type | Description |
|-----------|---------------------|---------------|--------------------|-------------|
| x     | Yes                 | None              | array-like             |X-coordinates|
| y     | Yes                 | None              | array-like             |Y-coordinates|
| s     | No                  | 20 (rcParam)      | scalar/array           |Marker size (s)|
| c     | No                  | None              | color/array            |Marker-color(c)|
| marker| No                  | 'o'               | str          |Marker-shape|
| cmap     | No                  | None              | str/colormap        |Colormap(used only if c is numeric array)|
| alpha     | No                  | None              | float(0-1)         |Transparency|

> **Questions to answer**
>
> - Which parameters are required?
_**x, y are required**_
> - Which parameters are optional?
_**s, c, marker, cmap, alpha; are all optional**_
> - What happens if you omit an optional parameter?
_**their default values are used**_
> - What default value is used?
_**s=20; c=default color from cycle; marker='o'; alpha=None(fully Opaque)**_

---

## Return Value

What does the function return?

**_a scatter plot_**

## Example

import matplotlib.pyplot as plt

x = (1, 2 ,3)
y = [2.5, 3.4, 4.5]

plt.scatter(x, y,
         c='red', s=20, alpha=None, label='first line', marker='x')
plt.show()
plt.legend()

<!-- or -->

np.random.seed(100)
x = np.random.rand(50)
y = np.random.rand(50)
plt.scatter(x, y, s=100, c='blue', alpha=0.5)
plt.show()

## Expected Output

a scatter plot

## What did you learn about this function?

Write one or two sentences describing something interesting you discovered.

**it's easy to understand**