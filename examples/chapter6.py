# -*- coding: utf-8 -*-
"""
Chapter 6: Sorting Data
Business Question:
Which employees stand out?
Functions to Learn:
sort_values()
sort_index()
nlargest()
nsmallest()
Exercises:
1. Sort employees by salary.
2. Display the ten highest-paid employees.
3. Display the ten youngest employees.
4. Display employees with the longest tenure.
"""

import pandas as pd

attrition = pd.read_csv('IBM Attrition.csv')

#sorting by salary
high_low = attrition['MonthlyIncome']
print(high_low.sort_values())

high_low2 = attrition['MonthlyRate']
print(high_low2.sort_values())

#10 highest paid employyes
print(high_low.nlargest(10))
print(high_low2.nlargest(10))

#10 highest paid employyes alternative
print(high_low.sort_values(ascending=False).head(10))
print(high_low2.sort_values(ascending=False).head(10))

#10 youngest employees
young = attrition['Age']
print(young.nsmallest(10))

#alternative
print(young.sort_values(ascending=True).head(10))

#longest tenure
tenure = attrition['YearsAtCompany']
print(tenure.nlargest().value_counts())

tenure2 = attrition['YearsInCurrentRole']
print(tenure2.nlargest().value_counts())

#alternative
print(tenure.sort_values(ascending=True).value_counts())
print(tenure2.sort_values(ascending=True).value_counts())