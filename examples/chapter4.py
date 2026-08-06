# -*- coding: utf-8 -*-
"""
Chapter 4: Selecting Variables
Business Question:
Which variables are important for our analysis?
Functions to Learn:
[]
loc[]
iloc[]
filter()
drop()
Exercises:
1. Display only Age.
2. Display Age and MonthlyIncome.
3. Display Age, Department and Attrition.
4. Create a new DataFrame for attrition analysis.
5. Remove EmployeeCount, StandardHours and EmployeeNumber.
"""

import pandas as pd

attrition = pd.read_csv('IBM Attrition.csv')

#showing all the column names
print(attrition.columns)

#displaying the age only
print(attrition['Age'])

#displaying the Age & Monthly INcome
print(attrition[['Age', 'MonthlyIncome']])

#displaying age, dept, attrition
print(attrition[['Age', 'Department', 'Attrition']])

#displaying age in specified row index 
print(attrition.loc[20, ['Age']])

#displaying age & monthly income in spcified row index
print(attrition.loc[0, ['Age', 'MonthlyIncome']])

#displaying value in specified column x row
print(attrition.iloc[20, 15])

#selecting first row
print(attrition.iloc[0])

# selecting first column
print(attrition.iloc[:, 0])

#filtering
print(attrition.filter(like='Rate'))

#dropping a row
print(attrition.drop(3))

#dropping a column
print(attrition.drop('Age', axis=1))

#reproducibility
print(attrition.sample(n=10, random_state=42))









