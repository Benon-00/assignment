# Function 11

## Function Name

```python
plt.title()
```

---

## Purpose

Describe what the function does.

_**Sets a title for the current axes**_


## Syntax

```python
plt.title(label, fontdict=None, loc='center', pad=None, **kwargs)
```

---

## Parameters

| Parameter | Required? (Yes/No) | Default Value | Expected Data Type | Description |
|-----------|---------------------|---------------|--------------------|-------------|
|label     | Yes                  |None          | str        |Title text|
|fontdict  | No                  |None          | dict        |Font properties|
|loc       | No     |'center'     | {'center', 'left', 'right'}    |Horizontal position|
|pad    | No      |None(rcParams, 6.0) | float     |Padding above the axes position|





> **Questions to answer**
>
> - Which parameters are required?
_**label is required**_
> - Which parameters are optional?
_**fontdict, loc, pad; are all optional**_
> - What happens if you omit an optional parameter?
_**they use their default values**_
> - What default value is used?
_**fontdict=None; pad=float; loc='center'**_

---

## Return Value

What does the function return?

**a line plot with the title**

## Example

import numpy as np

plt.plot([1,2,3])
plt.title("My Title")
plt.show()

## Expected Output

**a line plot with the title**

## What did you learn about this function?

Write one or two sentences describing something interesting you discovered.

**it's easy to implement*