# Function 16

## Function Name

```python
plt.savefig()
```

---

## Purpose

Describe what the function does.

_**Saves the currrent figure to a file(PNG, PDF, SVG, JPG, etc)**_


## Syntax

```python
plt.savefig(fname, dpi=None, format=None, bbox_inches=None, **kwargs)
```

---

## Parameters

| Parameter | Required? (Yes/No) | Default Value | Expected Data Type | Description |
|-----------|---------------------|---------------|--------------------|-------------|
|fname    | Yes   |None | str/Path/file-like     |Output filename or path|
|dpi      | No   |rcParams 'figure.dpi' (100) | float/'figure'    |Resolution|
|format   | No   |inferred from fname extension | str    |file format|
|bbox_inches    | No   |None | str/Bbox    |'tight' trims extra whitespace|
|transparent    | No   |False | bool    |Transparent background|


> **Questions to answer**
>
> - Which parameters are required?
_**fname is required**_
> - Which parameters are optional?
_**dpi; format; bbox_inches; transparent; all are optional**_
> - What happens if you omit an optional parameter?
_**they use their default values**_
> - What default value is used?
_**dpi=No; format=inferred from fname extension; bbox_inches=str; transparent=bool**_

---

## Return Value

What does the function return?

**writes file to disk*

## Example

import matplotlib.pyplot as plt

plt.plot([1,2,3])
plt.savefig("chart.png", dpi=300, bbox_inches='tight')
plt.show()


## Expected Output
**a line chart saved to my directory**

## What did you learn about this function?

Write one or two sentences describing something interesting you discovered.

**it's easy to understand**
