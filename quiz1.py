# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 10:13:22 2023

@author: bayst
"""

# quiz1.py
# Ding Xin
# U63555835
# CS108 A1

import math
import random

def cylinder_surface_area(radius, height):
    '''returns surface area of cylinder with given parameters
    a = 2(pi)rh + 2(pi)(r^2)'''
    
    # use pi constant from math fxn
    pi = math.pi
    
    return (2 * pi * radius * height) + (2 * pi * (radius ** 2))
    
def make_password(word, num, symbol):
    '''returns password with first 4 letters of word, num, the symbol, then rest of the word'''
    
    # assigning variable to 1st 4 letters of word
    name1 = word[0:4]
    
    # assigning variable to latter part of word
    # blank space in stop input tells the splicing operator to go all the way to the end of string
    name2 = word[4:]
    
    # use f-string to concatenate num (int) into password string
    return f'{name1}{num}{symbol}{name2}'

def get_random_date():
    '''calls random.randint fxn twice to return date in form of MM/DD
    MM: 0-12
    DD: 1-31'''
    
    # assign variables to randint fxns with proper parameters
    m = random.randint(1, 12)
    d = random.randint(1, 31)
    
    # use f-strings to put 0's in front of possible single digits
    return f'{m:02.0f}/{d:02.0f}'
    

if __name__ == '__main__':
    print('cylinder_surface_area(2, 2)', cylinder_surface_area(2, 2))
    print('make_password(beatles, 1962, !)', make_password('beatles', 1962, '!'))
    print('get_random_date()', get_random_date())