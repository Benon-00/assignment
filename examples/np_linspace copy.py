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
