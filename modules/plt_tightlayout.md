# Function 23

## Function Name

```python
plt.tight_layout()
```

---

## Purpose

Describe what the function does.

_**automatically adjusts subplot spacing/padding to prevent overlapping labels, titles and ticks**_

## Syntax

```python
plt.tight_layout(pad=1.08, h_pad=None, w_pad=None, rect=None)
```

---

## Parameters

| Parameter | Required? (Yes/No) | Default Value | Expected Data Type | Description |
|-----------|---------------------|---------------|--------------------|-------------|
|pad   |No   |1.08| float  | Overall padding (fraction of font size)|
|h_pad |No   |None (use pad)| float  | Height padding between subplots|
|w_pad |No   |None (use pad)| float  | Width padding between subplots|
|rect  |No   |None (whole figure, 0,0,1,1)| tuple  | Bounding box for layout|




> **Questions to answer**
>
> - Which parameters are required?
_**none is required**_
> - Which parameters are optional?
_**pad; h_pad; w_pad; rect; are optional**_
> - What happens if you omit an optional parameter?
_**they use their default values**_
> - What default value is used?
_**pad=1.08; h_pad=pad=w_pad; rect=0,0,1,1**_

---

## Return Value

What does the function return?

**a figure that adjusts layout real-time**

## Example

import matplotlib.pyplot as plt

plt.subplots(2, 2)
plt.tight_layout()
plt.show()


## Expected Output
**4-subplots within a 2x2 grid that no longer overlap; spacing is automatically adjusted*

## What did you learn about this function?

Write one or two sentences describing something interesting you discovered.

**this makes the plotting of graphs easier**







