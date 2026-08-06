# -*- coding: utf-8 -*-
"""
Chapter 3: Data Quality
Business Question:
Is our dataset clean enough to support reliable analysis?
Functions to Learn:
isna()
sum()
duplicated()
drop_duplicates()
nunique()
unique()
value_counts()
Exercises:
1. Does the dataset contain missing values?
2. Which variable has the most missing values?
3. Are there duplicate employees?
4. Remove duplicate observations.
5. Which variables have only one unique value?
6. Count employees in each department.
"""
import pandas as pd
import numpy as np

attrition = pd.read_csv('IBM Attrition')

#checking the column names
columns = attrition.columns
print(columns)

#1. checking for any misiing values
print(attrition.isna())
   #2 checking variable with the most missing values
print(attrition.isna().sum())


#check for duplicates 
print(attrition.duplicated())
print(attrition.duplicated().sum())

#remove duplicates
print(attrition.drop_duplicates())

#getting number of uniques value in whole dataset
print(attrition.nunique())
    #getting actual unique values of specified columns
print(attrition['NumCompaniesWorked'].unique())


#no. of employees per dept
print(attrition['Department'].value_counts())