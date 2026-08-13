## Example

import matplotlib.pyplot as plt
import numpy as np

np.random.seed(100)
data = np.random.rand(10, 10)
plt.imshow(data, cmap='hot', interpolation='bicubic', origin='upper', aspect='equal')
plt.colorbar(orientation='horizontal')
plt.show()









