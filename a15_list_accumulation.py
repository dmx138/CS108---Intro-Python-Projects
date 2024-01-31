# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 10:39:23 2023

@author: bayst
"""

# File: a15_list_accumulation.py
# your name: Ding Xin
# your email: dmx@bu.edu
# U63555835
# CS108 A1

def powers(base, n):
    '''builds a list of the first n powers of the base'''
    
    
    result = []
    
    # n + 1 so it exponentiates up to 10 not 9
    for i in range(n + 1):
        # print(i)
        
        powers = base ** i
        # print(powers)
        
        result += [powers]
    
    return result



def factors(n):
    '''returns a list of the all the factors of n'''


    result = []
    
    # 1 to n + 1 so we don't % by 0
    for i in range(1, n + 1):
        
        if n % i == 0:
            
            result += [i]
            
    return result



def get_uniques(items):
    '''returns a list with only one copy of each item in a given list'''
    
    uniques = []
    
    for i in items:
        # print(i)
        
        if i not in uniques:
            
            uniques += [i]
            
        
    return uniques





if __name__ == '__main__':
    # print('powers(2,10)', powers(2,10))
    print(factors(30))
    print(factors(20))
    words = ['to', 'be', 'or', 'not', 'to', 'be']
    numbers = [30, 5, 5, 20, 25, 35, 25, 20, 15, 25, 10, 15, 40, 10, 15, 10, 30, 20, 5, 40, 35, 30, 40, 35]
    # print(get_uniques(words))
    # print(get_uniques(numbers))