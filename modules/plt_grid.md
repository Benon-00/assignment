# Function 15

## Function Name

```python
plt.grid()
```

---

## Purpose

Describe what the function does.

_**Toggles and configures the gridlines on the current axes**_


## Syntax

```python
plt.grid(visible=None, which='major', axis='both', **kwargs)
```

---

## Parameters

| Parameter | Required? (Yes/No) | Default Value | Expected Data Type | Description |
|-----------|---------------------|---------------|--------------------|-------------|
|visible    | No   |None(toggles) | bool     |Show/hide gridlines|
|which      | No   |'major'| {'major', 'minor', 'both'} |which ticks get gridlinies|
|axis       | No   | 'both'| {'both', 'x', 'y'} |Which axis to apply to|
|color      | No   |rcParams | str    |Gridline color|
|linestyle  | No   |rcParams default | str     | Gridline style|





> **Questions to answer**
>
> - Which parameters are required?
_**none is required**_
> - Which parameters are optional?
_**all are optional**_
> - What happens if you omit an optional parameter?
_**plt.grid() tggles grid visibility on/off using major ticks on both axes with default style**_
> - What default value is used?
_**visibl=bool; which='major'; axis='both'; color=str; linestyle='str'**_

---

## Return Value

What does the function return?

**the function modifies the axes as requested*

## Example

import numpy as np

plt.plot([1,2,3])
plt.grid(True, which='both', axis='both', color='gray', linestyle='--')
plt.show()
## Expected Output

**the line plot's y-axis is fixed to span from 0 to 5, with the line compressed toward the bottom of the visible range**

## What did you learn about this function?

Write one or two sentences describing something interesting you discovered.

**a line plot overlaid with dashed gray gridlines on both axes