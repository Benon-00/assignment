# -*- coding: utf-8 -*-
"""
Chapter 5: Finding Employees
Business Question:
Which employees satisfy specific conditions?
Functions to Learn:
loc[]
query()
isin()
between()
str.contains()
str.startswith()
str.endswith()
&
|
~
Exercises:
1. Find employees who left the company.
2. Find employees in Sales.
3. Find employees earning more than $10,000.
4. Find employees younger than 30.
5. Find employees who worked overtime.
6. Find female employees in Sales.
7. Find employees with income between $4,000 and $8,000.
8. Find employees in Sales or Human Resources.
9. Find job roles containing 'Manager'.
10. Find employees who left and worked overtime.
"""
import pandas as pd

attrition = pd.read_csv('IBM Attrition.csv')

#initiating the columns
print(attrition.columns)

#those who left
exited = attrition[attrition['Attrition']== 'Yes']
print(exited['Attrition'].value_counts())

#alternative
print(attrition.loc[attrition['Attrition'] == 'Yes', 'Attrition'])

#those in sales
sales = attrition[attrition['Department']== 'Sales']
print(sales['Department'].value_counts())

#alternative2
sales2 = attrition.query("Department == 'Sales'")
print(sales2)

#alternative3
sales3 = attrition[attrition['Department'].isin(['Sales'])]
print(len(sales3))

#earning >$10,000 (using OR/ operator)
ten_thousand = attrition[(attrition['MonthlyIncome'] >10000)|(attrition['MonthlyRate'] >10000)]
print(len(ten_thousand))

#using AND& operator
ten_thousand2 = attrition[(attrition['MonthlyIncome'] >10000)&(attrition['MonthlyRate'] >10000)] 
print(len(ten_thousand2))


#below age 30
below_30 = attrition[attrition['Age'] <30]
print(len(below_30))


#overtime
overtime = attrition[attrition['OverTime']=='Yes']
print(len(overtime))

#females in sales
female_sales = attrition[(attrition['Gender']=='Female')&(attrition['Department']=='Sales')]
print(len(female_sales))


#earning btw $4,000-$8000 (using OR/ operator)
between1 = attrition[(attrition['MonthlyIncome'].between(4000, 8000))|(attrition['MonthlyRate'].between(4000, 8000))]
print(len(between1))

#using AND& operator
between2 = attrition[(attrition['MonthlyIncome'].between(4000, 8000))&(attrition['MonthlyRate'].between(4000, 8000))]
print(len(between2))


#employees in sales OR HR
sales_hr = attrition[(attrition['Department']=='Sales') | (attrition['Department']=='Sales')]
print(len(sales_hr))

#employees left & overtime
overtime_left = attrition[(attrition['Attrition']=='Yes') & (attrition['OverTime']=='Yes')]
print(len(overtime_left))

#containing manager
managers = attrition[attrition['JobRole'].str.contains('Manager')]
print(len(managers))

#startswith
managers2 = attrition[attrition['JobRole'].str.startswith('Ma')]
print(len(managers2))

#endswith
managers3 = attrition[attrition['JobRole'].str.endswith('ger')]
print(len(managers3))
