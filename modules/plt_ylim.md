# Function 14

## Function Name

```python
plt.ylim()
```

---

## Purpose

Describe what the function does.

_**Gets or sets the y-axis view limits of the current axes**_


## Syntax

```python
plt.ylim(*args, **kwargs)
```

---

## Parameters

| Parameter | Required? (Yes/No) | Default Value | Expected Data Type | Description |
|-----------|---------------------|---------------|--------------------|-------------|
|bottom       | No   |auto(data-based)   | float    |Lower y-limit|
|top      | No   |auto(data-based)   | float    |upper y-limit|






> **Questions to answer**
>
> - Which parameters are required?
_**none is required; calling with no arguments returns current limits**_
> - Which parameters are optional?
_**all are optional**_
> - What happens if you omit an optional parameter?
_**they use their default values**_
> - What default value is used?
_**auto-scaled limits based on plotted data**_

---

## Return Value

What does the function return?

**the line plot's y-axis spanning the limits*

## Example

import numpy as np

plt.plot([1,2,3])
plt.ylim(0, 5)
plt.show()

## Expected Output

**the line plot's y-axis is fixed to span from 0 to 5, with the line compressed toward the bottom of the visible range**

## What did you learn about this function?

Write one or two sentences describing something interesting you discovered.

**the data autoscales i.e in that, the plt.plot values given don't automatically fill the plt.ylim, but are auto-scaled*