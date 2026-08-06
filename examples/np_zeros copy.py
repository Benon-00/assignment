## Example

import numpy as np

base_data = ((2,3))
custom_array = np.zeros(
    shape=base_data, 
    dtype=np.float32, 
    order='F', 
    like=None)

print(custom_array)

