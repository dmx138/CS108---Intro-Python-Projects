#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 10:56:54 2023

@author: azs
"""

import pandas as pd

filename = 'annual_data.csv'
df = pd.read_csv(filename)




df['GDP'] #extracting one column

df[['GDP', 'CPI']] #extracting multiple columns

# set the index to be the values from the column 'Year'
df.index = df['Year']

# slicing by label (1960 to the end of records)
df['GDP'].loc[1960:]
# column-wise arithmetic

df['GDP'].loc[1960:] / 1000 

# create a new DataFrame; set the numeric index (for years)
df_new = pd.DataFrame(index=range(1960,2020))
# copy a column into the new DataFrame
df_new['GDP'] = df['GDP']
# shift all values in the column 'GDP' down by 1 row
df_new['GDP_prev'] = df_new['GDP'].shift(1)
# calculate the rate of change from the previous year's value
df_new['GDP_chg'] = df_new['GDP'] / df_new['GDP_prev'] - 1


