# Function 10

## Function Name

```python
plt.ylabel()
```

---

## Purpose

Describe what the function does.

_**sets the label text for the y-axis of the current axes**_


## Syntax

```python
plt.ylabel(ylabel, fontdict=None, labelpad=None, **kwargs)
```

---

## Parameters

| Parameter | Required? (Yes/No) | Default Value | Expected Data Type | Description |
|-----------|---------------------|---------------|--------------------|-------------|
|ylabel     | Yes                  |None          | str        |Label text|
|fontdict   | No                  |None          | dict        |Font properties|
|labelpad   | No                  |None (rcParams) | float     |Spacing between label and axis|
|loc   | No              |'center'       | {'left','center', 'right' }      |Label position|







> **Questions to answer**
>
> - Which parameters are required?
_**ylabel is required**_
> - Which parameters are optional?
_**fontdict, labelpad, loc; are all optional**_
> - What happens if you omit an optional parameter?
_**they use their default values**_
> - What default value is used?
_**fontdict=None; labelapad=None; loc='center'**_

---

## Return Value

What does the function return?

**a line plot with an ylabel**

## Example

import numpy as np

plt.plot([1,2,3])
plt.ylabel("Value")
plt.show()


## Expected Output

**a line plot with an ylabel**

## What did you learn about this function?

Write one or two sentences describing something interesting you discovered.

**it's easy to implement*