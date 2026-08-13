# Function 19

## Function Name

```python
plt.imshow()
```

---

## Purpose

Describe what the function does.

_**Displays image-like data (2D array or RGBA(A) array as an image on the Axes- used for images, heatmaps and matrices)**_

## Syntax

```python
plt.imshow(X, cmap=None, vmin=None, vmax=None, interpolation=None, **kwargs)
```

---

## Parameters

| Parameter | Required? (Yes/No) | Default Value | Expected Data Type | Description |
|-----------|---------------------|---------------|--------------------|-------------|
|X   |Yes   |None | array-like/PIL Image   |Image data (2D or 3D array)|
|cmap  |No   |'viridis' (rcParams) | str/Colormap  | Colormap for scalr data|
|vmin  |No   | data min | float   | Lower color-scale bound|
|vmax  |No   | data max | float   | Upper color-scale bound|
|interpolation |No | 'antialiased'(rcParams) | str   | Pixel interpolation method|


> **Questions to answer**
>
> - Which parameters are required?
_**X is required**_
> - Which parameters are optional?
_**cmap; vmin; vmax; interpolation; alpha; origin**_
> - What happens if you omit an optional parameter?
_**they use their default values**_
> - What default value is used?
_**cmap='viridis'; vmin=data-min; vmax=data-max; interpolation='antialiased'**_

---

## Return Value

What does the function return?

**an image**

## Example

import matplotlib.pyplot as plt

np.random.seed(100)
data = np.random.rand(10, 10)
plt.imshow(data, cmap='hot', interpolation='bicubic', origin='upper', aspect='equal')
plt.colorbar()
plt.show()


## Expected Output
**a 10 X 10 grid of colored cells shaded from dark to bright red, based on the random values, using a 'hot' colormap, with a colorbar legend*

## What did you learn about this function?

Write one or two sentences describing something interesting you discovered.

**one has to use the colorbar for ease of visualization of metrics**





