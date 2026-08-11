## Example

import matplotlib.pyplot as plt

values= [23, 44, 33]
Labels = ['A', 'B', 'C']

plt.pie(
    x=values,
    explode=None,
    labels=Labels,
    colors=['blue', 'green', 'yellow'],
    autopct='%1.1f%%',
    startangle=0
)

plt.show()
plt.legend()


