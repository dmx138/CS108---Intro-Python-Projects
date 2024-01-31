# -*- coding: utf-8 -*-
"""
Created on Sun Oct  1 18:23:48 2023

@author: bayst
"""

# File: a08_table_data.py
# your name: Ding Xin
# your email: dmx@bu.edu
# U63555835
# CS108 A1

def print_multiples_and_powers(x, n):
    '''displays first n multiples of x, and first n squared and cubed integers of x'''
    
    # fancy heading
    print(f'Here are the first {n} multiples and powers of {x}:')
    print(f'{"i":^8}{"i^2":^8}{"i^3":^8}')
    
    # iterate the amount of multiples and assign to i
    for i in range(1, n + 1):
        # print(f'i={i}')
        
        # iterate parameters x (assigned to j), i times
        for j in range(x, x + 1):
            print(f'{i * j:8}{(j * i) ** 2:8}{(i * j) ** 3:8}', end = '')
            
        print()
    
from a05_number_format import format_time

def print_marathon_pace_chart(hours, minutes):
    '''displays a marathon pace chart for a finish time of a given hours and minutes'''
    
    tm = (hours * 60) + minutes
    # print(tm)
    
    # heading
    goal_pace = (tm / 26.2) 
    print(f'GOAL TIME: {format_time(tm)}')
    print(f'GOAL PACE: {format_time(goal_pace)}')
    print(f'{"Mile":^8}{"Time":^8}')
    
    # iterate over each whole mile and assign to i (first half, 1-13)
    for i in range(1, 14):
        # assign format_time to a variable so it can be concatenated in printout with an f-string
        time = format_time(goal_pace * i)
        print(f'{i:^8}{time:^8}')
        
    # print the halfway time (13.2)
    half_time = format_time(tm / 2)
    print(f'{"HM 13.1":^8}{half_time:^8}')
    
    # print out the the 2nd half with assignment, j (14-26)
    for j in range(14, 27):
        time = format_time(goal_pace * j)
        print(f'{j:^8}{time:^8}')
    
    # finally, print out finish time (26.2)
    finish_time = format_time(tm)
    print(f'{"HM 26.2":^8}{finish_time:^8}')
    
    


if __name__ == '__main__':

    # print_multiples_and_powers(3, 10)
    print_marathon_pace_chart(4, 40)