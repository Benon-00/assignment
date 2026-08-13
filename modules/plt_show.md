# Function 17

## Function Name

```python
plt.show()
```

---

## Purpose

Describe what the function does.

_**displays all open figures (blocks execution in non-intercative backends until windows are closed)**_


## Syntax

```python
plt.show(*, block=None)
```

---

## Parameters

| Parameter | Required? (Yes/No) | Default Value | Expected Data Type | Description |
|-----------|---------------------|---------------|--------------------|-------------|
|block   |No   |None(True for non-interactive backends) | bool   |Whether to block script execution|



> **Questions to answer**
>
> - Which parameters are required?
_**the section of plot code to show is required**_
> - Which parameters are optional?
_**block**_
> - What happens if you omit an optional parameter?
_**matplotlib decides blocking behaviour auomatically based on the backend in use**_
> - What default value is used?
_**block=None**_

---

## Return Value

What does the function return?

**a window pop-up**

## Example

import matplotlib.pyplot as plt

plt.plot([1,2,3])
plt.show()


## Expected Output
**a window pop-up having a line chart**

## What did you learn about this function?

Write one or two sentences describing something interesting you discovered.

**it's easy to understand**

