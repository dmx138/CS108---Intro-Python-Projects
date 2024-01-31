# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 08:59:45 2023

@author: bayst
"""

# Ding Xin
# dmx@bu.edu
# U63555835
# CS108

import pandas as pd

def double_upper_case(s):
    '''procs a string and doubles all uppper case letters, then lowercases the whole word'''
    
    # set up an accumulator for a string
    new_string = ''
    
    # start by iterating over each letter in the string
    for ch in s:

        # check if ch is a letter first
        if 97 <= ord(ch) <= 122 or 65 <= ord(ch) <= 90:
            
            # check if the ch is uppercased or not
            if ch == ch.upper():
                
                new_string += ch * 2
                
            # if it's lowercased
            elif ch == ch.lower():
            
                new_string += ch
            
        # print non-letters as normal
        else:
            
            new_string += ch
            
            
    # return lowercased accumulator
    return new_string.lower()
            

class Volume:
    '''data object that represents a liquid volume and string scale'''
    
    # initialize the object's variables
    def __init__(self, value, scale):
        
        self.value = value
        self.scale = scale
        
        
    # repr prints the object out in a neatly formatted string
    def __repr__(self):
        
        # printout for gallons
        if self.scale == 'G':
            
            return f'{self.value} gallons'
            
        # printout for liters
        if self.scale == 'L':
            
            return f'{self.value} liters'
        
        
    # converts gallons to liters
    def value_in_liters(self):
        
        # if the class is already in liters, simply return the value
        if self.scale == 'L':
            
            return self.value
        
        # if the class is in gallons, convert to liters
        if self.scale == 'G':
            
            return self.value * 3.8
    
    
    # overrider for == operator
    def __eq__(self, other):
        
        # call value_in_liters on both self and other and compare, if True return True
        if self.value_in_liters() == other.value_in_liters():
            
            return True
        
        # if False return False, mind boggling
        elif self.value_in_liters() != other.value_in_liters():
        
            return False
        
    
def show_relative_values(df, columns, start, end):
    '''procs a df of annual data from a start year to an end year and computes the value of each column relative to the start year'''
    
    # create a new dataframe
    df_rv = pd.DataFrame(index = df.index)
    
    
    # iterate through the list of columns
    for c in columns:
        
        # create new data series in the new df that are the same values as df[c] but divided by the values of the start year
        df_rv[f'{c}'] = df[c] / df[c].loc[start]
   
    
    # plot the new df
    df_rv.loc[start:end].plot(title = 'relative values')
    



if __name__ == '__main__':
    # print(double_upper_case('abc XYZ'))
    # print(double_upper_case('Hello, Goodbye.'))
    
    v1 = Volume(5, 'G') # evaluates to 10 gallons
    # print(v1)
    v2 = Volume(19, 'L')
    # print(v2)
    # print(v1.value_in_liters())
    # print(v1 == v2)
    
    df = pd.read_csv('data.csv')
    df.index = df['Year']
    columns = ['IncomePct20', 'IncomePct80', 'MedianHouse']
    show_relative_values(df, columns, 2000, 2020)