## Example

import numpy as np

arr = np.array([1,2,3,4,5])
print(np.mean(arr))

# or 

matrix = np.array([[1,2,6], [4,8,12]]) #a
mask = (matrix % 2 == 0) #where
output_array = np.empty((2,1), dtype=np.float64) #keepdims & out

np.mean(
    a= matrix,
    axis=1, 
    dtype=np.float64, 
    out=output_array, 
    keepdims=True, 
    where=mask)

print(output_array)

