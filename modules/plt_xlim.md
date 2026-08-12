# Function 13

## Function Name

```python
plt.xlim()
```

---

## Purpose

Describe what the function does.

_**Gets or sets the x-axis view limits of the current axes**_


## Syntax

```python
plt.xlim(*args, **kwargs)
```

---

## Parameters

| Parameter | Required? (Yes/No) | Default Value | Expected Data Type | Description |
|-----------|---------------------|---------------|--------------------|-------------|
|left       | No   |auto(data-based)   | float    |Lower x-limit|
|right      | No   |auto(data-based)   | float    |upper x-limit|






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

**the line plot's x-axis spanning 0 to 5**

## Example

import numpy as np

plt.plot([1,2,3])
plt.xlim(0, 5)
plt.show()

## Expected Output

**the line plot's x-axis is fixed to span from 0 to 5, adding blank space beyond the data**

## What did you learn about this function?

Write one or two sentences describing something interesting you discovered.

**the data autoscales i.e in that, the plt.plot values given don;t automatically fill the plt.xlim, but are auto-scaled*