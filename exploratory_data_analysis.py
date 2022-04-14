#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 19:15:17 2021

@author: pj athul
""" 

import os
import pandas as pd
import numpy as np

a=pd.read_csv('Toyota.csv',index_col=0,na_values=["??","????"])
b=a.copy()

#Frequency Table

frequency_table=pd.crosstab(index=b['FuelType'],columns='count',dropna=True)
print(frequency_table) #here only one categorical value is considered
#FuelType is the category considered

#Two way table
#More than 1 category is considered

two_way_table=pd.crosstab(index=b['Automatic'],columns=b['FuelType'],
                          dropna=True)
print("\n \n")
print(two_way_table)

# Two way table  - Joint probability
# Convert table values from number to proportions 

ttj=pd.crosstab(index = b['Automatic'],
                columns=b['FuelType'],
                normalize=True,
                dropna=True)
print("\n \n")
print(ttj)

#Two way table - Marginal Probability
#It is the probability of single event
# We get sum of row values and column values

mp=pd.crosstab(index = b['Automatic'],
               columns = b['FuelType'],
               margins = True,
               normalize = True,
               dropna = True)

print("\n\n Marginal Probability \n")
print(mp)

#Two way table - Conditional Probability
cp=pd.crosstab(index = b['Automatic'],columns = b['FuelType'],
               margins = True, normalize = 'index',
               dropna = True)

print("\n\n Conditional Probability  Row Sum is 1\n") # is Row sum is 1
print(cp)
print("\n Conditional Probability where the Column Sum =1\n")

cp1=pd.crosstab(index = b['Automatic'],
                columns = b['FuelType'],
                margins = True,
                dropna= True,
                normalize = 'columns') #It gives column sum as 1

print(cp1) 

#Correlation

#selec only numerical data
numerical_data=b.select_dtypes(exclude=['object'])
print(numerical_data.shape)

#correlation matrix

cm=numerical_data.corr()
print("\n\n Correlation Matrix \n")
print(cm)
