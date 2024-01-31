# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 10:10:43 2023

@author: bayst
"""

# File: quiz2.py
# your name: Ding Xin
# your email: dmx@bu.edu
# U63555835
# CS108 A1

def product_between(start, end):
    '''calculates and returns the product of all integers between start and end'''
    
    # accumulator variable, can't be 0 because we're multiplying
    product = 1
    
    # accumulate results with a loop
    for i in range(start, end + 1):
        # print(i) # prints 3-6
        
        product *= i
        
        
    # return accumulated product
    return product



def count_double_letters(s):
    '''processes a string and returns a count of adjacent letters'''
    
    # set up accumulator variable for the count
    count = 0
    
    # index-based loop to iterate over every character
    for i in range(len(s)):
        # print(i) # prints 0-3
        # print(s[i]) # prints b o o k
            
            # check for adjacent chrs
        if (2 * s[i]) in s:
                
                count += 1
          
    # return the count
    # count // 2 to account for double counts
    return count // 2




def print_ascii_table():
    '''prints out a neatly formatted table of numeric codes (48-127) and there corresponding ASCII characters'''
    '''8 x 10 table'''

    # set up columns
    for i in range(10):
        # print(i)
        
        x = 48 + (i * 8)
        # print(x) # 48 to 120 in increments of 8
        
        # print(f'{x}')
        
        # set up rows 
        for j in range(8):
            # print(j)
            y = x + j
            # print(y)
            
            print(f'{y:6}: {chr(y)}', end = ' ')
            # print(j + x, end = '')
    # for i in range(10):
        
    #     for j in range(8):
            
    #         value = ((48 + (i * 8)) + j)
            
    #         print(f'{value:6}: {chr(value)}', end = ' ')
        
        

            





if __name__ == '__main__':
    # print(product_between(3, 6))
    # print(product_between(0, 3))
    # print(count_double_letters('book'))
    # print(count_double_letters('bookkeeper'))
    print_ascii_table()
