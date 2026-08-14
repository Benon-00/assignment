# Function 22

## Function Name

```python
plt.annotate()
```

---

## Purpose

Describe what the function does.

_**adds a text annotation with an optional arrow pointing from the text to a specific data point**_

## Syntax

```python
plt.annotate(text, xy, xytext=None, arrowprops=None, **kwargs)
```

---

## Parameters

| Parameter | Required? (Yes/No) | Default Value | Expected Data Type | Description |
|-----------|---------------------|---------------|--------------------|-------------|
|text   |Yes   | - | str  | Annotation text|
|xy   |Yes   | - | tuple(x, y)  | Point being annotated|
|xytext   |No   | same as xy | tuple (x, y)  | Location of the text|
|arrowprops  |No   | None (No arrow drawn)| dict  | Arrow style properties|
|xycoords   |No   | 'data' | str  | Coordinate system for xy|



> **Questions to answer**
>
> - Which parameters are required?
_**text, xy; are required**_
> - Which parameters are optional?
_**xytext; arrowprops; xycoords; are optionaln**_
> - What happens if you omit an optional parameter?
_**text is placed directly at xy with no arrow drawn (since xytext defaults to xy and no arrow appears without arrowprops)**_
> - What default value is used?
_**xytext=xy; arrowprops=None; xycoords='data'**_

---

## Return Value

What does the function return?

**an annotated xy coordinate**

## Example

import matplotlib.pyplot as plt

x= [1, 2, 3]
y= [1, 4, 9]

plt.plot(x, y)
plt.annotate('max', xy=(3,9), 
             xytext=(2,7), arrowprops=dict(facecolor='black', shrink=0))
plt.show()


## Expected Output
**an annoatatd xy coordinate, with an arrow prop*

## What did you learn about this function?

Write one or two sentences describing something interesting you discovered.

**it's simple to visualize**







