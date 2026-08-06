# Chapter 1: Importing Data
# Business Question:
# HR has provided the IBM Employee Attrition dataset. How do we load it into Python so we can begin our analysis?
# Functions to Learn:
# import pandas as pd
# pd.read_csv()
# head()
# tail()
# shape
# columns
# info()
# Exercises:
# 1. Import the pandas library.
# 2. Read the IBM Attrition dataset.
# 3. Display the first five records.
# 4. Display the last five records.
# 5. How many employees are in the dataset?
# 6. How many variables are available?
# 7. Display the names of all variables.
# 8. Display the structure of the dataset.

import pandas as pd
import numpy as np

# Load the data
file = pd.read_csv('IBM Attrition.csv')

# Print DataFrame Head
print(file.head(7))
print('-' * 150)

# Print DataFrame Tail
print(file.tail(7))
print('-' * 150)

# Print DataFrame Shape
print(file.shape)
print('-' * 150)

# Print DataFrame Columns
print(file.columns)
print('-' * 150)

# Print DataFrame Info
file.info()
