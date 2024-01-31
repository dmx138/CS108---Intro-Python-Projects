# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 00:45:27 2023

@author: bayst
"""

# File: a09_accumulator.py
# your name: Ding Xin
# your email: dmx@bu.edu
# U63555835
# CS108 A1

def sum_of_range(start, stop, skip):
    '''accumulates and returns the sum of range(start, stop, skip)'''
    
    # (1) set up an accumulator variable
    total = 0
    
    # (2) set up loop to collect numbers added to sum
    for i in range(start, stop, skip):
        # print(i) matches up with the set given in test cases
        
        num = i
        
        total += num
        # print(total)
        
    # (3) accumulate after loop is done w/ a print statement
    return total

import random

def estimate_pi(n):
    '''estimates value of pi w/ definite loop and accumulator
    
    imagine a circle inscribed to the edges of a square (1x1, with the origin at the center)
    
    the ratio of circle area : square area is equal to
    
    # of darts that land in the circle : # of darts thrown
    
    so area of circle = (# circle darts * square area) / total darts
    
    then we get pi'''
    
    # (1) set up an accumulator variable
    hits = 0 
    
    # (2) use loops to collect hits
    for i in range(1, n + 1):
        # print(i)
        # use random.uniform() to return random hits within the circle area
        x = random.uniform(-1.0, 1.0)
        
        y = random.uniform(-1.0, 1.0)
        
        # if x^2 + y^2 <= 1.0, it has hit the circle
        
        dart = (x ** 2) + (y ** 2)
        
        # (3) accumulate hits
        
        if dart <= 1.0:
            
            hits += 1
            
        # area of circle = (# circle darts * square area) / total darts
        
        circle_area = (hits * (2.0 ** 2)) / i
        
        # area of circle = pi * r^2
        
        pi_estimate = circle_area / (1.0 ** 2)
        
        print(f'{hits} out of {i} throws so that pi is {pi_estimate}')
        
    return pi_estimate

def double_daily(initial_amount, number_of_days):
    '''What's better? 100$ a day for a month, or 1 cent on day 1, 2 cents on day 2, 4 cents on day 3 etc.
    this fxn will return a initial dollar amount doubled each day over a period of a given number of days'''
    
    # (1) accumulator variable
    
    total = initial_amount
    daily_amount_earned = initial_amount
    
    # printout heading, day 1 is printed out beforehand because we want it unchanged from our accumulating loop
    
    print(f'day{"daily amount":^25}total')
    print(f'1{"$":^10}        {initial_amount:.2f} ${initial_amount:^27.2f}')
    
    # (2) use loops to collect values
    # start with 2 so the first day isn't doubled
    
    for i in range(2, number_of_days + 1):
        # print(i) prints 2-10
        
        daily_amount_earned = daily_amount_earned * 2
        # print(daily_amount_earned)
        
        total += daily_amount_earned
        # print(total)
        
        # (3) accumulate values into a printout
        
        print(f'{i}{"    $"}{daily_amount_earned:17.2f} ${total:^27.2f}')
        
    return total
        
        
        
if __name__ == '__main__':
    # print('sum_of_range(1,5,1)', sum_of_range(1,5,1)) # adds the numbers [1, 2, 3, 4]
    # sum_of_range(10,20,2) # adds the numbers [10, 12, 14, 16, 18]
    # print('estimate_pi(10)', estimate_pi(10))
    print('estimate_pi(100)', estimate_pi(100))
    # print('double_daily(1, 10)', double_daily(1, 10))