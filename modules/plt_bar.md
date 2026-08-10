# Function 3

## Function Name

```python
plt.bar()
```

---

## Purpose

Describe what the function does.

_**Creates a vertical bar chart**_


## Syntax

```python
plt.bar(x, height, width=0.8, bottom=None, align='center', *kwargs)
```

---

## Parameters

| Parameter | Required? (Yes/No) | Default Value | Expected Data Type | Description |
|-----------|---------------------|---------------|--------------------|-------------|
| x         | Yes                 | None              | array-like/scalar  |X-coordinates|
| height    | Yes               | None              | array-like/scalar  |Heights of bars|
| width     | No                | 0.8              | float/array  |Width of bars|
| bottom    | No                | 0              | array-like/scalar  |Y-coordinates of bar base (where the x-ais starts from)|
| align     | No                | 'center'       | 'center', 'edge'   |Bar alignment relative to x|
| color     | No                | Next in cycle  |str/array  |Bar-colors(s)|


> **Questions to answer**
>
> - Which parameters are required?
_**x, height; are required**_
> - Which parameters are optional?
_**width, bottom, align, color; are all optional**_
> - What happens if you omit an optional parameter?
_**their default values are used**_
> - What default value is used?
_**width=0.8; bottom=0; align=center; color=Next in cycle**_

---

## Return Value

What does the function return?

**a bar chat**

## Example

import numpy as np

x = (1, 2 ,3)
y = [2.5, 3.4, 4.5]

plt.bar(x, y,
        width= 0.2, bottom=0, align='center', color='green')
plt.show()
plt.legend()


## Expected Output

a bar vertical chart

## What did you learn about this function?

Write one or two sentences describing something interesting you discovered.

**easy to apply**