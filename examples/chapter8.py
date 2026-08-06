# -*- coding: utf-8 -*-
"""
Chapter 8: Summarising Data
Business Question:
What does our workforce look like overall?
Functions to Learn:
mean()
median()
mode()
std()
min()
max()
agg()
count()
Exercises:
1. Calculate the average age.
2. Calculate the average monthly income.
3. Find the median monthly income.
4. Find the highest monthly income.
5. Calculate the standard deviation of age.
6. Count the employees.
"""

import pandas as pd


attrition = pd.read_csv('IBM Attrition.csv')

#1. getting mean
print(attrition['Age'].mean())
print('\n' + ('-'*50) + '\n')

#to 2 decimal places
print(round(attrition['Age'].mean(), 2))
print('\n' + ('-'*50) + '\n')

#mode
print(attrition['Age'].mode())
print('\n' + ('-'*50) + '\n')



# 2. getting avg income
print(round(attrition['MonthlyIncome'].mean(), 2))
print('\n' + ('-'*50) + '\n')

#median income
print(round(attrition['MonthlyIncome'].median(), 2))
print('\n' + ('-'*50) + '\n')

#mode
print(round(attrition['MonthlyIncome'].mode(), 2))
print('\n' + ('-'*50) + '\n')

#highest monthly income
print(round(attrition['MonthlyIncome'].max(), 2))
print('\n' + ('-'*50) + '\n')

#std of age
print(round(attrition['Age'].std(), 2))
print('\n' + ('-'*50) + '\n')

#count of employees
print(attrition.count())

print(attrition['Age'].agg(['mean', 'median', 'max', 'min']))





