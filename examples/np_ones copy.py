## Example

import numpy as np

base_data = ((2,3))
custom_array = np.ones(
    shape=base_data, 
    dtype=np.int32, 
    order='C', 
    like=None)

print(custom_array)

