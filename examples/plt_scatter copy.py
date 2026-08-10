## Example

import matplotlib.pyplot as plt

x = (1, 2 ,3)
y = [2.5, 3.4, 4.5]

plt.scatter(x, y,
         c='red', s=20, alpha=None, label='first line', marker='x')
plt.show()
plt.legend()

# <!-- or -->

np.random.seed(100)
x = np.random.rand(50)
y = np.random.rand(50)
plt.scatter(x, y, s=100, c='blue', alpha=0.5)
plt.show()

