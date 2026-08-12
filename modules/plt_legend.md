# Function 12

## Function Name

```python
plt.legend()
```

---

## Purpose

Describe what the function does.

_**Places a legend on the axes, using labels defined via label= in plotting calls (or explicitly passed)**_


## Syntax

```python
plt.legend(*args, loc=None, fontsize=None, ncol=1, **kwargs)
```

---

## Parameters

| Parameter | Required? (Yes/No) | Default Value | Expected Data Type | Description |
|-----------|---------------------|---------------|--------------------|-------------|
|label     | No   |auto-detected from label=    | list of str     |Legend entry text|
|handles   | No   |auto-detected | list of Artist  |Objects to level|
|loc       | No   | 'best'| str/int/tuple |Legend location|
|ncol      | No   |1  | int   |Number of columns|





> **Questions to answer**
>
> - Which parameters are required?
_**none is required; matplotlib auto-collects labels**_
> - Which parameters are optional?
_**all are optional**_
> - What happens if you omit an optional parameter?
_**they use their default values**_
> - What default value is used?
_**label=autodetected; handles=autodetected; loc='best'; ncol=1**_

---

## Return Value

What does the function return?

**a line plot with the legend**

## Example

import numpy as np

plt.plot([1,2,3], label='line A')
plt.legend(loc='best')
plt.show()

## Expected Output

**a line plot with the label legend on the upper left**

## What did you learn about this function?

Write one or two sentences describing something interesting you discovered.

**it's easy to implement*