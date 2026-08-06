# Chapter 2: Exploring the Dataset
# Business Question:
# Before analysing employee attrition, what does our dataset look like?
# Functions to Learn:
# describe()
# describe(include='object')
# dtypes
# info()
# sample()
# memory_usage()
# Exercises:
# 1. Display summary statistics for numeric variables.
# 2. Display summary statistics for categorical variables.
# 3. Which variable has the highest maximum value?
# 4. Display a random sample of 10 employees.
# 5. Which variables are integers?
# 6. How much memory is the dataset using?

import pandas as pd
import numpy as np

# Load the data
file = pd.read_csv('IBM Attrition.csv')
categorical_variables = file.dtypes[file.dtypes=='string'].index

# Print Statistical summary of numerical variables
print("\nthese are the numerical stats\n")
print(file.describe())
print('-' * 150)

# Print Statistical summary of object variables
print("\nthese are the categorical stats\n")
print(file[categorical_variables].describe())
print('-' * 150)

# Print Variable with MAX values
print("\nthese are the max values for each column\n")
print(file.max(numeric_only=True))
print('-' * 150)

# Print Variable with MAX value
print("\nthis is the variable with the MAX value\n")
overall_max_column = file.max(numeric_only=True).idxmax()
print(overall_max_column)
print('-' * 150)

# Print Random Numbers of 10 employees
print("\nthese are the random numbers\n")
print(file.sample(10))
print('-' * 150)

# Print Info structure of the dataset
file.info()
