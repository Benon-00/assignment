# -*- coding: utf-8 -*-
"""
Chapter 7: Creating New Variables
Business Question:
Can we derive more useful information from the existing data?
Functions to Learn:
assign()
apply()
lambda
np.where()
cut()
qcut()
Exercises:
1. Create an Age Group variable.
2. Create an Income Category.
3. Create a Retirement Status variable.
4. Create a High Risk Attrition variable.
5. Categorize employees into salary quartiles.
"""

import pandas as pd
import numpy as np

attrition = pd.read_csv('IBM Attrition.csv')

print(attrition.columns)

#figuring out what the functions do
"""
1. .assign()Used to add new columns to a DataFrame without modifying the original data. It always returns a new DataFrame copy.

2. A lambda function is a quick, one-line anonymous function used for simple calculations on the fly.

3. .apply()Used to pass every value in a column through a function (often a lambda function) to transform the data.

4. np.where() Works like an IF-THEN-ELSE statement. It checks a condition: if true, it gives value A; if false, it gives value B.

5. pd.cut()Divides continuous numbers into bins based on specific, custom-defined numeric ranges.

6. pd.qcut()Divides data into bins based on sample quantiles (percentages). It automatically finds the boundaries so that every bin contains roughly the same number of rows.

"""

# 1. Add a column for Monthly Income converted to Yearly Income using .assign()
yearly_income = attrition.assign(YearlyIncome = attrition['MonthlyIncome']*12)
print(yearly_income[['MonthlyIncome', 'YearlyIncome']].head(3))
print('\n' + ('-'*50) + '\n')

#2. A simple lambda that divides 5 to any input x
divide_five = lambda x:x/5
print(divide_five(100))

#3. Divide every age by 10 using apply and lambda
Age_Decade = attrition.assign(Age_Decade = attrition['Age'].apply(lambda x:x/10))
print(Age_Decade[['Age_Decade', 'Age']].head(3))
print('\n' + ('-'*50) + '\n')

#4. If Income is over 10000 mark as 'High', otherwise 'Standard'
Income_Tier = attrition.assign(Income_Tier = np.where(attrition['MonthlyIncome']>10000, 'High', 'Standard'))
print(Income_Tier[['MonthlyIncome', 'Income_Tier']].sort_values(by='MonthlyIncome', ascending=False).head(4))
print('\n' + ('-'*50) + '\n')

#5 Define custom boundaries and labels
boundaries = [0, 30, 50, 100]
age_labels = ['Young', 'Middle-Aged', 'Senior']

# Split the Age column into these exact ranges
Age_Group = attrition.assign(Age_Group= pd.cut(attrition['Age'], labels=age_labels, bins=boundaries))
print(Age_Group[['Age', 'Age_Group']].head(4))
print('\n' + ('-'*50) + '\n')


#6. Split income into 4 equal-sized groups (Quartiles: 25% of rows each)
income_labels = ['Low', 'Medium', 'High', 'Top']
Income_Bracket = attrition.assign(Income_Bracket = pd.qcut(attrition['MonthlyIncome'], q=4, labels=income_labels))
print(Income_Bracket[['Income_Bracket', 'MonthlyIncome']].sort_values(by='MonthlyIncome', ascending=False).head(5))
print('\n' + ('-'*50) + '\n')


"""
Chapter 7: Creating New Variables
Business Question:
Can we derive more useful information from the existing data?
Functions to Learn:
assign()
apply()
lambda
np.where()
cut()
qcut()
Exercises:
1. Create an Age Group variable.
2. Create an Income Category.
3. Create a Retirement Status variable.
4. Create a High Risk Attrition variable.
5. Categorize employees into salary quartiles.
"""
#create an agegroup variable
Age_Group = attrition.assign(Age_Group = attrition['Age']*1.5)
print(Age_Group[['Age_Group', 'Age']].head(5))
print('\n' + ('-'*50) + '\n')

#income category
Income_category = attrition.assign(Income_category = attrition['MonthlyRate'].apply(lambda x:x*10))
print(Income_category[['Income_category', 'MonthlyRate']].head(5))
print('\n' + ('-'*50) + '\n')

#alternative income category
labels = ['low', 'medium', 'high', 'very high']
Income_category = attrition.assign(Income_category = pd.qcut(attrition['MonthlyRate'], q=4, labels=labels))
print(Income_category[['Income_category', 'MonthlyRate']].head(5))
print('\n' + ('-'*50) + '\n')

#retirement status
retired = attrition.assign(retired = np.where(attrition['Age']> 60, 'Retired', 'Working'))
print(retired[['Age', 'retired']].tail(5))

#attriton risk
attrition_risk = attrition.assign(attrition_risk = np.where(attrition['Attrition']=='Yes', 'Very High', 'low'))
print(attrition_risk[['Attrition', 'attrition_risk']].head(10))