## Example

import matplotlib.pyplot as plt

x= [1, 2, 3]
y= [1, 4, 9]

plt.plot(x, y)
plt.annotate('max', xy=(3,9), 
             xytext=(2,7), arrowprops=dict(facecolor='black', shrink=0))
plt.show()









