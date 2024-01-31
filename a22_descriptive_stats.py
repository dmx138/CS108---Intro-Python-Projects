# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 10:21:20 2023

@author: bayst
"""

# File: a22_descriptive_stats.py
# your name: Ding Xin
# your email: dmx@bu.edu
# U63555835
# CS108 A1

import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
from a21_data_analytics import *


def plot_column_with_rolling_mean(df, column_name, window = 10):
    '''procs a df and plots the values for a column along with is rolling mean'''
    
    # create a new df
    df_rm = pd.DataFrame(index=df.index)
    # print(df_rm)
    # result = []
    
    # check if columns are valid
    # if column_name not in df.columns and type(df[column_name].iloc[-1]) != str:
    #     # print(test)
    #     # result += [f'{column_name}_rm']
    #     df_rm[f'{column_name}_rm'] = df[column_name].rolling(window).mean()
        
    #     # result += [f'{column_name}_rm']
        
    #     return df_rm[f'{column_name}_rm'].plot()
    
    # else:
    
        # df_result = df[column_name].iloc[0:]
    # check for errors first
    if column_name not in df.columns:
        
        print(f'Invalid column name `{column_name}`.')
        
        return 
        
    if type(df[column_name].iloc[-1]) == str:
        
        print('Error: string column data')
        
        return 
            
    # if parameters pass errors, proceed as normal
    elif column_name in df.columns and type(df[column_name].iloc[-1]) != str:
                # print(c)
                
        # result += [f'{column_name}_rm']
        df_rm[f'{column_name}_rm'] = df[column_name].rolling(window).mean()
                
        # result += [f'{column_name}_rm']
    # print(df_rm)
    

       
    # print(result)
    # plot both the original data and the rolling mean data
    df[column_name].plot()
    df_rm[f'{column_name}_rm'].plot()
    


def create_scatter_plot(df, x_column_name, y_column_name):
    '''creates a scatterplot with given x and y parameters'''
    
    result = []
    
    if x_column_name in df.columns and type(df[x_column_name].iloc[-1]) != str:
        
        result += [x_column_name]
        
    # check if columns are valid
    elif x_column_name not in df.columns or type(df[x_column_name].iloc[-1]) == str:
        
        print(f'Invalid column name `{x_column_name}`. \nValid columns are: {result}.')
        # print(f'Invalid column name {x_column_name}')
        # print(f'Valid columns are: {result}.')
    
    
    if y_column_name in df.columns and type(df[y_column_name].iloc[-1]) != str:
            
        result += [y_column_name]
        
    # check if columns are valid
    elif y_column_name not in df.columns or type(df[y_column_name].iloc[-1]) == str:
            
        print(f'Invalid column name `{y_column_name}`. \nValid columns are: {result}.')
    
    
    if x_column_name in df.columns and type(df[x_column_name].iloc[-1]) != str and y_column_name in df.columns and type(df[y_column_name].iloc[-1]) != str:
    
        plt.xlabel(x_column_name)
        plt.ylabel(y_column_name)
        plt.scatter(df[x_column_name], df[y_column_name])
        

def do_regression(df, independent, dependent):
    '''performs OLS regression with independent as the x-axis and dependent as the y-axis'''
    
    result = []
    
    if independent in df.columns and type(df[independent].iloc[-1]) != str:
        
        result += [independent]
        print(result)
    # check if columns are valid
    elif independent not in df.columns or type(df[independent].iloc[-1]) == str:
        
        print(f'Invalid column name `{independent}`. \nValid columns are: {result}.')
        # print(f'Invalid column name {x_column_name}')
        # print(f'Valid columns are: {result}.')
    
    
    if dependent in df.columns and type(df[dependent].iloc[-1]) != str:
            
        result += [dependent]
        
    # check if columns are valid
    elif dependent not in df.columns or type(df[dependent].iloc[-1]) == str:
            
        print(f'Invalid column name `{dependent}`. \nValid columns are: {result}.')
    
    
    if independent in df.columns and type(df[independent].iloc[-1]) != str and dependent in df.columns and type(df[dependent].iloc[-1]) != str:
        # set x and y variables
        X = df[independent]
        Y = df[dependent]
        
        # perform the regression
        model = sm.OLS(Y, X).fit()
        print(model.summary())
        P = model.predict()
        # create_scatter_plot(df, X, Y)
        plt.xlabel(independent)
        plt.ylabel(dependent)
        plt.scatter(X, Y)
        plt.plot(X, P, color = 'red')

if __name__ == '__main__':

    filename = 'annual_data.csv'

    # read the data, set up index
    df = pd.read_csv(filename)
    df.index = df['Year']
    
    df_result = calculate_rates_of_change(df, ['GDP', 'CPI'])
    # print(df_result)
    # print(type(df_result['GDP_chg'].iloc[1]))
    # print(df_result.tail())
    # print(df_result.head())
    # plot_column_with_rolling_mean(df_result, 'GDP_chg', 5)
    # create_scatter_plot(df_result, 'GDP_chg', 'CPI_chg')
    # create_scatter_plot(df_result, 'GDP_chg', 'MedianHouse_chg')
    do_regression(df_result.loc[1963:2021], 'GDP_chg', 'CPI_chg')
    
    
    #### work for a22_report ####
    
    # Question 1
    # df_result = calculate_rates_of_change(df, ['CPI', 'SP500', 'MedianHouse', 'IncomePct20', 'IncomePct80'])
    # df_result.plot()
    
    # Question 2
    # df_result = calculate_rates_of_change(df, ['CPI', 'SP500', 'IncomePct80'])
    # print(df_result)
    
    # df_result = plot_column_with_rolling_mean(df_result, 'CPI_chg', 5)
    # plt.ylabel('CPI_chg', fontsize = 15)
    # df_result.plot()
    
    # df_result = plot_column_with_rolling_mean(df_result, 'SP500_chg', 5)
    # plt.ylabel('SP500_chg', fontsize = 15)
    # df_result.plot()
    
    # plot_column_with_rolling_mean(df_result, 'IncomePct80_chg', 5)
    # plt.ylabel('IncomePct80_chg', fontsize = 15)
    # df_result.plot()
    
    # Question 3
    # df_result = calculate_rates_of_change(df, ['MedianHouse', 'IncomePct95', 'IncomePct40', 'IncomePct60', 'MinimumWage', 'SP500', 'CPI', 'IncomePct80', 'IncomePct20', 'GDP', 'Population'])
    
    # a.
    plt.xlabel('GDP_chg', fontsize = 15)
    plt.ylabel('MedianHouse_chg', fontsize = 15)
    # do_regression(df_result.loc[1970:2020], 'GDP_chg', 'MedianHouse_chg')
    # R2 = 0.654
    
    # b.
    # plt.xlabel('IncomePct60_chg', fontsize = 15)
    # plt.ylabel('IncomePct80_chg', fontsize = 15)
    # do_regression(df_result.loc[1970:2020], 'IncomePct60_chg', 'IncomePct80_chg')
    # R2 = 0.977
    
    # c.
    # plt.xlabel('IncomePct40_chg', fontsize = 15)
    # plt.ylabel('IncomePct20_chg', fontsize = 15)
    # do_regression(df_result.loc[1970:2020], 'IncomePct40_chg', 'IncomePct20_chg')
    # R2 = 0.938
    
    # d.
    # plt.xlabel('Population_chg', fontsize = 15)
    # plt.ylabel('SP500_chg', fontsize = 15)
    # do_regression(df_result.loc[1970:2020], 'Population_chg', 'SP500_chg')
    # R2 = 0.229