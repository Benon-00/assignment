# Function 6

## Function Name

```python
plt.pie()
```

---

## Purpose

Describe what the function does.

_**Creates a pie chart representing a proportion of the whole**_


## Syntax

```python
plt.pie(x, explode=None, labels=None, colors=None, autopct=None, startangle=0, **kwargs)
```

---

## Parameters

| Parameter | Required? (Yes/No) | Default Value | Expected Data Type | Description |
|-----------|---------------------|---------------|--------------------|-------------|
|x          | Yes                 | None          | array-like         |Wedge sizes (relative)|
|explode    | No                  | None          | array-like         |Offset of each wedge from center|
|labels     | No                  | None          | list of str         |Labels fro each wedge|
|colors     | No                  | None (cycle)  | list of str         |Wedge colors |
|autopct    | No                  | None          | str/function        |Format string for percentage labels|
|startangle | No                  | 0             | float         |Rotation of start of first wedge (degrees)|



> **Questions to answer**
>
> - Which parameters are required?
_**x is required**_
> - Which parameters are optional?
_**exlode, labels, colors, autopct, startangle; are all optional**_
> - What happens if you omit an optional parameter?
_**they use their default values**_
> - What default value is used?
_**explode=None; labels=None; colors=None; autopct=None; startangle=0**_

---

## Return Value

What does the function return?

**a pie-chart**

## Example

import numpy as np

values= [23, 44, 33]
Labels = ['A', 'B', 'C']

plt.pie(
    x=values,
    explode=None,
    labels=Labels,
    colors=['blue', 'green', 'yellow'],
    autopct='%1.1f%%',
    startangle=0
)

plt.show()
plt.legend()


## Expected Output

a pie-chart

## What did you learn about this function?

Write one or two sentences describing something interesting you discovered.

**one needs to be keen to realize that the values x nhave to add up to 100!**