# Function 5

## Function Name

```python
np.linspace()
```

---

## Purpose

Describe what the function does.

_**Returns evenly spaced numbers over a specified interval, with control over the exact count of samples (unlike arange, which uses step size)**_


## Syntax

```python
np.linspace(start, stop, num-=50, endpoint=True, retstep=False, dtype=None, axis=0)
```

---

## Parameters

| Parameter | Required? (Yes/No) | Default Value | Expected Data Type | Description |
|-----------|---------------------|---------------|--------------------|-------------|
| start     | Yes                 | None          | array_like        |Starting value of the sequence|
| stop     | Yes                 | None          | array_like        |End value of the sequence|
| num     | No                 | 50          | int        |Number of samples to generate|
| endpoint     | No                 | True          | boolean        |Wherther to include stop in the output|
| retstep     | No                 | False         | boolean        |Whether to return the stp size used|
| dtype     | No                 | None          | data-type        |Type of output array; inferred if not given|
| axis     | No                 | 0          | int        | axis along which to store the sample|




> **Questions to answer**
>
> - Which parameters are required?
_**start, stop are required**_
> - Which parameters are optional?
_**num, endpoint, retstep, dtype, axis are all optional**_
> - What happens if you omit an optional parameter?
_**num defaults to 50; endpoint defaults to True, retstep defaults to False, dtype defaults to None; axis defaults to 0**_
> - What default value is used?
_**num=50; endpoint=True; retstep=False; dtype=None; axis=0**_

---

## Return Value

What does the function return?

**_float radians_**

## Example

import numpy as np

custom_array = np.linspace(
    start=0,
    stop=10,
    num=100,
    endpoint=True,
    retstep=False,
    dtype=np.float64,
    axis=0
)
print(custom_array)
print(custom_array.dtype)

## Expected Output

[ 0.          0.1010101   0.2020202   0.3030303   0.4040404   0.50505051
  0.60606061  0.70707071  0.80808081  0.90909091  1.01010101  1.11111111
  1.21212121  1.31313131  1.41414141  1.51515152  1.61616162  1.71717172
  1.81818182  1.91919192  2.02020202  2.12121212  2.22222222  2.32323232
  2.42424242  2.52525253  2.62626263  2.72727273  2.82828283  2.92929293
  3.03030303  3.13131313  3.23232323  3.33333333  3.43434343  3.53535354
  3.63636364  3.73737374  3.83838384  3.93939394  4.04040404  4.14141414
  4.24242424  4.34343434  4.44444444  4.54545455  4.64646465  4.74747475
  4.84848485  4.94949495  5.05050505  5.15151515  5.25252525  5.35353535
  5.45454545  5.55555556  5.65656566  5.75757576  5.85858586  5.95959596
  6.06060606  6.16161616  6.26262626  6.36363636  6.46464646  6.56565657
  6.66666667  6.76767677  6.86868687  6.96969697  7.07070707  7.17171717
  7.27272727  7.37373737  7.47474747  7.57575758  7.67676768  7.77777778
  7.87878788  7.97979798  8.08080808  8.18181818  8.28282828  8.38383838
  8.48484848  8.58585859  8.68686869  8.78787879  8.88888889  8.98989899
  9.09090909  9.19191919  9.29292929  9.39393939  9.49494949  9.5959596
  9.6969697   9.7979798   9.8989899  10.        ]
float64

## What did you learn about this function?

Write one or two sentences describing something interesting you discovered.

**when retstep=True, the dtype=None brings an attribute error**