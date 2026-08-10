## Example
import matplotlib.pyplot as plt

data = np.random.randn(1000)
plt.hist(data, bins=30, color='purple')
plt.show()

# or

# 1. Prepare raw input data (x)
scores = [55, 62, 67, 71, 74, 78, 81, 85, 89, 92, 95, 98, 105, 115]

# 2. Plot the histogram utilizing all explicit and kwargs parameters
n, bins_edges, patches = plt.hist(
    x=scores,
    bins=5,
    range=(60, 100),
    density=True,
    cumulative=True,
    color="skyblue",  # Passed via **kwargs
    edgecolor="black",  # Passed via **kwargs
    alpha=0.75,  # Passed via **kwargs
)

# Display the cumulative density plot
plt.title("Cumulative Probability Density of Test Scores")
plt.xlabel("Score Range")
# Force the chart's x-ticks to match the exact mathematical boundaries of the bins
plt.xticks(bins_edges)
# Access the 3rd bar (index 2) directly and turn it red
patches[2].set_facecolor("red")

plt.ylabel("Cumulative Probability")
plt.show()

# Find out the maximum probability or frequency calculated
print(f"The highest bin value is: {max(n)}")

