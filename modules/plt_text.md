# Function 21

## Function Name

```python
plt.text()
```

---

## Purpose

Describe what the function does.

_**adds an arbitrary text at a specified (x,y) data coordinate on the axes**_

## Syntax

```python
plt.text(x, y, s, fontdict=None, **kwargs)
```

---

## Parameters

| Parameter | Required? (Yes/No) | Default Value | Expected Data Type | Description |
|-----------|---------------------|---------------|--------------------|-------------|
|x   |Yes   | - | float  | X data coordinate|
|y   |Yes   | - | float  | Y data coordinate|
|s   |Yes   | - | str  | The text string|
|fontdict   |No   | None | dict  | Font overide properties|
|fontsize   |No   | rcParams | int/str  | Text size|
|ha(horizontalalignment) |No  | 'left' | str  | Horizontal alignment |



> **Questions to answer**
>
> - Which parameters are required?
_**x, y, s are required**_
> - Which parameters are optional?
_**fontdict; fontsize; ha; are optionaln**_
> - What happens if you omit an optional parameter?
_**they use their default values**_
> - What default value is used?
_**fontdict=NOne; fontsize=rcParams; ha='left'**_

---

## Return Value

What does the function return?

**a text object**

## Example

import matplotlib.pyplot as plt

x= [1, 2, 3]
y= [4,10, 17]

plt.plot(x, y)
plt.text(1.5, 2, 'Peak here', fontsize=12, color='red')
plt.show()


## Expected Output
**the text appears on the x-axis*

## What did you learn about this function?

Write one or two sentences describing something interesting you discovered.

**it almost functions like the plt.xlabel(); but this is specific to coordinates**







