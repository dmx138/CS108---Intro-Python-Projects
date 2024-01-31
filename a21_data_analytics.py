# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 10:53:02 2023

@author: bayst
"""

# File: a21_data_analytics.py
# your name: Ding Xin
# your email: dmx@bu.edu
# U63555835
# CS108 A1

import pandas as pd

# df.head() shows first 5 rows and all columns
# df.columns() returns a list of all column names
# df['GDP'] returns first and last 5 rows of a column (series), multiple columns can be extracted (dataframe)

def plot_columns(df, columns = None):
    '''plots the given column parameters into a graph'''

    # if no columns are given 
    if columns == None and type(df[columns].iloc[-1]) != str:
        
        df.plot()
    
    # if a column name is an invalid column, i.e. not in df.columns
    else:
    
        
        for c in columns:
            # print(c)
            if c in df.columns and type(df[c].iloc[-1]) != str:
                
                df[c].plot()

            

def calculate_standardized_values(df, base_index, columns = None):
    '''procs a df object and returns the values as a % relative to 1
    the year given as base_index will have a value of 1'''
    
    
    # set the index range of our specific dataframe to df.index
    df_std = pd.DataFrame(index=df.index)
    
    result = []
    
    # check if columns are valid
    if columns == None and type(df[columns].iloc[-1]) != str:
        
        df_std[f'{columns}_std'] = df_std[columns] / df[columns].loc[base_index]
        
        result += [f'{columns}_std']
        
        return df_std[result]
    
    else:
    
        df_std = df[columns].iloc[0:]
        
        for c in columns:
            
            if c in df.columns and type(df[c].iloc[-1]) != str:
                # print(c)
                # column-wise arithmetic
                df_std[f'{c}_std'] = df_std[c] / df_std[c].loc[base_index]
                
                result += [f'{c}_std']
                # c = c + '_std'
                
            
    return df_std[result]
    


        
def calculate_rates_of_change(df, columns = None):
    '''goes through each column and returns the annual rate of change between that year's value and the next year'''
    
    # set the index range of our specific dataframe to df.index
    df_chg = pd.DataFrame(index=df.index)
    
    result = []
    
    # check if columns are valid
    if columns == None and type(df[columns].iloc[-1]) != str:
        
        df_chg[f'{columns}_chg'] = df_chg[columns] / df_chg[columns].shift(1) - 1
        
        result += [f'{columns}_chg']
        
        return df_chg[result]
    
    # if valid, proceed with column-wise arithmetic
    else:
        
        df_chg = df[columns].iloc[0:]
        
        for c in columns:
            
            if c in df.columns and type(df[c].iloc[-1]) != str:
                # print(c)
                # column-wise arithmetic
                df_chg[f'{c}_chg'] = df_chg[c] / df[c].shift(1) - 1
                
                result += [f'{c}_chg']
                # c = c + '_std'
                
            
    return df_chg[result]
    
    # our arithemetic-wise calculations
    # df_new = df['CPI'].tail() / df['CPI'].shift().tail() - 1

    # print(df_new)



if __name__ == '__main__':

    filename = 'annual_data.csv'

    # read the data, set up index
    df = pd.read_csv(filename)
    
    # indexes our data by the year
    df.index = df['Year']
    
    # print(plot_columns(df, ['GDP', 'CPI']))
    print(plot_columns(df, ['GDP', 'asidfiasdf']))
    # plot_columns(df, ['IncomePct20', 'IncomePct40', 'IncomePct60', 'IncomePct80', 'IncomePct95'])
    # df_std = calculate_standardized_values(df, 1980, ['GDP', 'CPI'])
    # print(df_std.loc[1975:1985])
    
    # df_std.plot()
    
    # df_chg = calculate_rates_of_change(df, ['GDP', 'CPI'])
    # print(df_chg.loc[1975:1985])
    
    # df_chg.plot()
    
    # calculate_rates_of_changes(df, ['CPI'])
    # df['GDP'] #extracting one column

    # df[['GDP', 'CPI']] #extracting multiple columns

    # set the index to be the values from the column 'Year'
    # df.index = df['Year']

    # # slicing by label (1960 to the end of records)
    # df['GDP'].loc[1960:]
    # # column-wise arithmetic

    # df['GDP'].loc[1960:] / 1000 

    # # create a new DataFrame; set the numeric index (for years)
    # df_new = pd.DataFrame(index=range(1960,2020))
    # # copy a column into the new DataFrame
    # df_new['GDP'] = df['GDP']
    # # shift all values in the column 'GDP' down by 1 row
    # df_new['GDP_prev'] = df_new['GDP'].shift(1)
    # # calculate the rate of change from the previous year's value
    # df_new['GDP_chg'] = df_new['GDP'] / df_new['GDP_prev'] - 1
    
    
    #### work for a21_report ####
    
    # # Question 1
    
    # df['GDP per capita'] = df['GDP'] / df['Population'] * 1000000000
    
    # print(df['GDP per capita'].iloc[-60:])
    
    # df['GDP per capita'].plot()
    
    # Question 2
    
    # df_std = calculate_standardized_values(df, 1980, ['MinimumWage', 'GDP'])
    
    # print(df_std.loc[1968:])
    
    # df_std.plot()
    
    # Question 3 
    
    # df_std = calculate_standardized_values(df, 1980, ['MedianHouse', 'GDP'])
    
    # print(df_std.loc[1963:])
    
    # df_std.plot()
    
    # Question 4 
    
    # df_std = calculate_standardized_values(df, 1980, ['MedianHouse', 'GDP'])
    
    # df_std.loc[1972:2022].plot()
    
    # Question 5 
    
    # df_std = calculate_standardized_values(df, 1980, ['MedianHouse', 'IncomePct20', 'IncomePct40', 'IncomePct60', 'IncomePct80', 'IncomePct95'])
    
    # df_std.loc[1972:2022].plot()
