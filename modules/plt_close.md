# Function 24

## Function Name

```python
plt.close()
```

---

## Purpose

Describe what the function does.

_**closes a figure window, freeing memory; important in loops that generate many figures**_

## Syntax

```python
plt.close(fig=None)
```

---

## Parameters

| Parameter | Required? (Yes/No) | Default Value | Expected Data Type | Description |
|-----------|---------------------|---------------|--------------------|-------------|
|fig   |No   |current figure| None/int/Figure/'all'  | Which figure(s) to close|




> **Questions to answer**
>
> - Which parameters are required?
_**none is required**_
> - Which parameters are optional?
_**fig is optional**_
> - What happens if you omit an optional parameter?
_**closes only the current active figure**_
> - What default value is used?
_**fig = None**_

---

## Return Value

What does the function return?

**None**

## Example

import matplotlib.pyplot as plt

plt.plot([1,2,3])
plt.savefig("chart.png", dpi=300, bbox_inches='tight')
plt.close()


## Expected Output
**the figure is saved to the directory, then all open figure windows/objects are closed and memory is released; nothing further is displayed*

## What did you learn about this function?

Write one or two sentences describing something interesting you discovered.

**it cannot be used together with plt.show()**







