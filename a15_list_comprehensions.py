# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 11:16:48 2023

@author: bayst
"""

# File: a15_list_comprehensions.py
# your name: Ding Xin
# your email: dmx@bu.edu
# U63555835
# CS108 A1

def triple(values):
    '''returns a list with all items tripled'''
    
    result = [i * 3 for i in values]
    
    return result



def powers(b, n):
    '''returns a list of the first n powers of base b'''
    
    result = [b ** i for i in range(n)]

    return result



def factors(n):
    '''returns a list of all factors of n'''
    
    # first i inputs the i into the result
    # but only if i is a factor of n (%)
    # range is given as 1 to n + 1 so it doesn't % by 0 and give an error
    result = [i for i in range(1, n + 1) if n % i == 0]
    
    return result



def num_vowels(s):
    '''returns the count of all vowels in a string'''
    
    count = len([1 for l in s if l in 'aeiouyAEIOUY'])
    
    return count
    
    
    



if __name__ == '__main__':
    # print(triple([1,2,3]))
    # print(triple(['a','b','c']))
    # print(triple(['python']))
    # print(triple('python'))
    # print(powers(2, 10))
    # print(powers(3, 8))
    # print(factors(30))
    print(num_vowels('multicollinearity'))