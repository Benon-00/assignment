# Function 4

## Function Name

```python
plt.barh()
```

---

## Purpose

Describe what the function does.

_**Creates a horizontal bar chart**_


## Syntax

```python
plt.barh(y, width, height =0.8, left=None, align='center', **kwargs)
```

---

## Parameters

| Parameter | Required? (Yes/No) | Default Value | Expected Data Type | Description |
|-----------|---------------------|---------------|--------------------|-------------|
| y         | Yes                 | None          | array-like/scalar  |Y-coordinats of bars|
| width     | Yes                 | None          | array-like/scalar  |bar lenghts|
| height    | No                  |0.8            | float/array        |thickness of bars|
| left      | No                  |0              | array-like/scalar  |X-coordinate of bar base|
| align     | No                  |'center'       | 'center', 'edge'   |Alignment|



> **Questions to answer**
>
> - Which parameters are required?
_**y, width are required**_
> - Which parameters are optional?
_**height, left, align; are all optional**_
> - What happens if you omit an optional parameter?
_**their default values are used**_
> - What default value is used?
_**height=0.8; left=0; align='center'**_

---

## Return Value

What does the function return?

*a horizontal bar-chart**

## Example

import matplotlib.pyplot as plt

x = (1, 2 ,3)
y = [2.5, 3.4, 4.5]

plt.barh(x, y,
        height= 1, left=0, align='center', color='green')
plt.show()
plt.legend()



## Expected Output

a horizontal bar chart

## What did you learn about this function?

Write one or two sentences describing something interesting you discovered.

**it's easy to implement**