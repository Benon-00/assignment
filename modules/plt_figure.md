# Function 8

## Function Name

```python
plt.figure()
```

---

## Purpose

Describe what the function does.

_**Creates a new figure (the top-level container for all plot elements) or activates an existing one**_


## Syntax

```python
plt.figure(num=None, figsize=None, dpi=None, facecolor=None, **kwargs)
```

---

## Parameters

| Parameter | Required? (Yes/No) | Default Value | Expected Data Type | Description |
|-----------|---------------------|---------------|--------------------|-------------|
|num        | No                  | auto-incremented int    | int/str  |Figure identifier|
|figsize    | No                  | (6.4, 4.8 )  | tuple |Width, height in inches|
|dpi        | No                  | 100         | float  |Dots per inch|
|facecolor  | No                  | 'white'     | str  |background color|



> **Questions to answer**
>
> - Which parameters are required?
_**none is required (all have defaults)**_
> - Which parameters are optional?
_**all are optional**_
> - What happens if you omit an optional parameter?
_**they use their default values**_
> - What default value is used?
_**num=incremental; figsize=(6.4, 4.8); dpi=100; facecolor='white'**_

---

## Return Value

What does the function return?

**a line plot on a grey background**

## Example

import numpy as np

plt.figure(
    num='Apple',
    dpi=100,
    figsize=(8, 6), 
    facecolor='lightgray')

plt.plot([1,2,3])
plt.show()


## Expected Output

a line plot on a grey background

## What did you learn about this function?

Write one or two sentences describing something interesting you discovered.

**it's an interesting function**