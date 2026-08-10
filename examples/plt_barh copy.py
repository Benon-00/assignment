## Example

import matplotlib.pyplot as plt

x = (1, 2 ,3)
y = [2.5, 3.4, 4.5]

plt.barh(x, y,
        height= 1, left=0, align='center', color='green')
plt.show()
plt.legend()

