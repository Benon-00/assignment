# Function 20

## Function Name

```python
plt.colorbar()
```

---

## Purpose

Describe what the function does.

_**adds a colorbar to a figure, mapping colors to data values, typically used alongside imshow(), scatter(), contourf()**_

## Syntax

```python
plt.colorbar(mappable=None, cax=None, ax=None, orientation='vertical', **kwargs)
```

---

## Parameters

| Parameter | Required? (Yes/No) | Default Value | Expected Data Type | Description |
|-----------|---------------------|---------------|--------------------|-------------|
|mappable   |No   |Image/artist in current Axes | ScalarMapple  |The object the colorbar is based on|
|cax   |No   |None (auto-created) | Axes | Axes to draw the colorbar in|
|ax   |No   | current Axes | Axes | Parent Axes(s) to steal space from|
|orientation   |No   | 'vertical' | {'vertical, 'horizontal'} | Bar orientation |


> **Questions to answer**
>
> - Which parameters are required?
_**none; matplotlib infers the mappable from the last image collection plotted**_
> - Which parameters are optional?
_**all are optionaln**_
> - What happens if you omit an optional parameter?
_**colorbar auto-attaches the most recent color-mapped artist, placed vertically at the right, in a new auto-sized axes**_
> - What default value is used?
_**mappable=Infers; cax=NOne; ax=current axes; orientation='vertical'**_

---

## Return Value

What does the function return?

**a colorbar object**

## Example

import matplotlib.pyplot as plt

np.random.seed(100)
data = np.random.rand(10, 10)
plt.imshow(data, cmap='hot', interpolation='bicubic', origin='upper', aspect='equal')
plt.colorbar(orientation='horizontal')
plt.show()


## Expected Output
**a heatmap image with a horizontal colorbar below it, showing the value-to-color mapping*

## What did you learn about this function?

Write one or two sentences describing something interesting you discovered.

**it's easy to interpret it when used alongside a heatmap**







