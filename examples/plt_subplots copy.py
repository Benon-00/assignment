## Example

import matplotlib.pyplot as plt

fig, axs = plt.subplots(2, 2, figsize=(10, 4))

# Indexing as [row, column]
axs[0, 0].plot([1, 2, 3])                           # Top-left
axs[0, 1].bar(['a', 'b'], [3, 5])                     # Top-right
axs[1, 0].scatter([3, 7, 8, 9], [0.4, 0.7, 0.9, 0.1]) # Bottom-left
axs[1, 1].hist([3, 7, 8, 9], align='mid', cumulative=True)  # Bottom-right
plt.show()


