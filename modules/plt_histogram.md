# Function 5

## Function Name

```python
plt.hist()
```

---

## Purpose

Describe what the function does.

_**Computes and plots a histogram of a dataset, showing frequency distribution across bins**_


## Syntax

```python
plt.hist(x, bins=None, range=None, density=False, cumulative=False, **kwargs)
```

---

## Parameters

| Parameter | Required? (Yes/No) | Default Value | Expected Data Type | Description |
|-----------|---------------------|---------------|--------------------|-------------|
|x          | Yes                 | None          | array-like         |Inupt data|
|bins       | No                  | 10            | int/sequence/str   |Numbers or edges of bins|
|range      | No                 | (min(x), max(x))   | tuple         |lower/upper ranges of bins|
|density    | No                 | False          |bool         |Normalize to form probability density|
|cumulative | No                 | False          | bool        |Plot cumulative histogram|
|color      | No                 | Next  in cycle | str         |Fill color|



> **Questions to answer**
>
> - Which parameters are required?
_**x is required**_
> - Which parameters are optional?
_**bins, range, density, cumulative, color; are all optional**_
> - What happens if you omit an optional parameter?
_**they use their default values**_
> - What default value is used?
_**sbins=10; range=min/max x; density=False; cumulative=Falase; color=next in cycle*_

---

## Return Value

What does the function return?

**a histogram**

## Example

import numpy as np

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

## Expected Output

a cumulative histogram

## What did you learn about this function?

Write one or two sentences describing something interesting you discovered.

**needs a lot of care when using it**