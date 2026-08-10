## Example

import matplotlib.pyplot as plt

x = (1, 2 ,3)
y = [2.5, 3.4, 4.5]

plt.bar(x, y,
        width= 0.2, bottom=0, align='center', color='green')
plt.show()
plt.legend()


