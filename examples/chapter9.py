# -*- coding: utf-8 -*-
"""
Chapter 9: Grouping Data
Business Question:
How do employee characteristics differ across groups?
Functions to Learn:
groupby()
agg()
size()
count()
mean()
median()
reset_index()
Exercises:
1. Calculate the average salary by department.
2. Calculate the average age by gender.
3. Calculate the average years at the company by marital status.
4. Count employees by department.
5. Calculate attrition rate by department.
6. Which department has the highest average salary?
"""

import pandas as pd

attrition = pd.read_csv('IBM Attrition.csv')

#1. avg salary by dpt
sal_dpt = attrition.groupby('Department')[['MonthlyIncome', 'MonthlyRate']].agg('mean')
print(round(sal_dpt))
print('-'*50)

sal_dpt = attrition.groupby('Department')[['MonthlyIncome', 'MonthlyRate']].agg('mean')
sal_dpt_flat = sal_dpt.reset_index() #resetting it to behave like a column in the results
print(round(sal_dpt_flat))
print('-'*50)

sal_dpt2 = attrition.groupby('Department')[['MonthlyIncome', 'MonthlyRate']].mean()
print(round(sal_dpt2))
print('-'*50)

#2. avg age by gender
age_gender = attrition.groupby('Gender')['Age'].mean()
print(round(age_gender))
print('-'*50)

#3. avg yrs by marital
atcompany_marital = attrition.groupby('MaritalStatus')['YearsAtCompany'].mean()
print(round(atcompany_marital))
print('-'*50)

#4. employees by dpt
employeesnumber_dpt = attrition.groupby('Department').size()
print(employeesnumber_dpt)
print('-'*50)

employeesnumber_dpt = attrition.groupby('Department').size()
employeesnumber_dpt_flat = employeesnumber_dpt.reset_index()
print(employeesnumber_dpt_flat)
print('-'*50)

employeesnumber_dpt = attrition.groupby('Department').count()
print(employeesnumber_dpt)
print('-'*50)

#5. attrition rate by dpt
attrition_dpt = attrition.groupby('Department')['Attrition']
print(attrition_dpt.count())
print('-'*50)

attrition_dpt2 = attrition.groupby('Department')['Attrition'].count()
print(attrition_dpt2)
print('-'*50)

#agg() & dept
highsal_dept = attrition.groupby('Department')[['MonthlyIncome', 'MonthlyRate']].agg(['max', 'min'])
print(highsal_dept)