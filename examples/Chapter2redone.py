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
import random

attrition = pd.read_csv('IBM Attrition.csv')

#summary statistics of numeric variables
print(attrition.describe())
print('Numerical summary stats')
print('\n'+ ('-' * 50) + '\n')

#getting -number of rows and columns
print(attrition.shape)
print(attrition.dtypes.value_counts())
print('rows x columns')
print('\n'+ ('-' * 50) + '\n')

# 2. Display summary statistics for categorical variables.
categorical = attrition.dtypes[attrition.dtypes == 'string'].index
print(attrition [categorical].describe())
print('Objects summary stats')
print('\n'+ ('-' * 50) + '\n')

# getting 10 random rows
print(attrition.sample(10))
print('random numbers')
print('\n'+ ('-' * 50) + '\n')

# getting the strucutre of the dataset
print(attrition.info())
print('strucute of dataset')
print('\n' + ('-'*50) + '\n')

#creating a subset of those who stayed
not_exited = attrition[attrition['Attrition']=='No']
print(not_exited.shape)
print('\n' + ('-'*50) + '\n')

#creating a subset of those who left
exited = attrition[attrition['Attrition']=='Yes']
print(exited.shape)
print('\n' + ('-'*50) + '\n')

#gettting count of non-numerical variables
print(attrition['YearsAtCompany'].value_counts())
print('\n' + ('-'*50) + '\n')

#creating a subset
over_twenty_years = attrition[[attrition['YearsAtCompany']] >= 20]
print(over_twenty_years['YearsAtCompany'].value_counts())
print('\n' + ('-'*50) + '\n')

# column names
print(attrition.columns)
print('\n' + ('-'*50) + '\n')

#creating subset by columns
attrition_subset = attrition[['Age', 'EducationField', 'JobSatisfaction']]
print(attrition_subset.describe(include='all'))
print('\n' + ('-'*50) + '\n')

#subset by common names
subset_names = attrition.filter(like='Rate')
print(subset_names.columns)
print('\n' + ('-'*50) + '\n')