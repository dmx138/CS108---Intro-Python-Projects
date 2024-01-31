# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 23:25:44 2023

@author: bayst
"""

# File: a10_rational_root.py
# your name: Ding Xin
# your email: dmx@bu.edu
# U63555835
# CS108 A1


def square_root(x):
    '''approximates the square root of x and returns the result as a function'''
    
    # (a) find the upper bound for the square root
    
    k = 1 # k should be >= to square root (x)
    
    while (k ** 2) < x:
        k += 1
        # print(k)
    
    # (b) check for a perfect square
    
    if (k ** 2) == x:
        print(f'({k}, 1)')
        return (k, 1)
        
    # (c) prepare for the iteration when k^2 =/= x
    
    lower_numerator = k - 1
    lower_denominator = 1
    lower_bound = (f'{lower_numerator}/{lower_denominator}')
    # print('low =', lower_bound)
        
    upper_numerator = k
    upper_denominator = 1
    upper_bound = (f'{upper_numerator}/{upper_denominator}')
    # print('up=', upper_bound)
        
        # recalled within loop
    test = 0
        # print('test =', test)
        
    diff = x - test
        # print('diff =', diff)
    
    # (d) do the iteration until we have a result that is close enough
    
    # when diff is negative, up becomes mid
    # when diff is positive, down becomes mid
    
    while diff > 0.01 or diff < -0.01:
        
        # move inside loop
        mid_numerator = lower_numerator + upper_numerator
        mid_denominator = lower_denominator + upper_denominator
        mid_point = (f'{mid_numerator}/{mid_denominator}')
        # print('mid =', mid_point) prints 7/2
        
        # recall test
        test = (mid_numerator / mid_denominator) ** 2
        # print(test) prints 12.25
        
        # reset diff
        diff = x - test
        # print(diff)
        
        # diff is negative, up reassigned to current mid
        if diff < 0:
            
            # redefine upper bound
            upper_numerator = mid_numerator
            upper_denominator = mid_denominator
            upper_bound = f'{mid_numerator}/{mid_denominator}'
        
            # do NOT redefine the midpoint, it's already being redefined at lines 59-61
        
            # print everything
            print(f'low = {lower_bound}, up = {upper_bound}, mid = {mid_point}, test = {test:.6f}, diff = {diff:0.6f}')
            
        
        # diff is positive, low reassigned to current mid
        if diff > 0:
            
            # redfine lower bound
            lower_numerator= mid_numerator
            lower_denominator = mid_denominator
            lower_bound = f'{mid_numerator}/{mid_denominator}'
            
            # do NOT redefine the midpoint, it's already being redefined at lines 59-61
            
            # printprintprint
            print(f'low = {lower_bound}, up = {upper_bound}, mid = {mid_point}, test = {test:.6f}, diff = {diff:0.6f}')
        
    # once diff is within +- 0.01, our while statement becomes false, then goes to this return statement        
    return (mid_numerator, mid_denominator)
            
if __name__ == '__main__':
    # square_root(25)
    # square_root(26)
    # square_root(10)
    square_root(144)