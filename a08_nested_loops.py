# -*- coding: utf-8 -*-
"""
Created on Sun Oct  1 20:19:39 2023

@author: bayst
"""

# File: a08_nested_loops.py
# your name: Ding Xin
# your email: dmx@bu.edu
# U63555835
# CS108 A1

def print_products(m, n):
    '''prints multiplication table of m times n'''
    
    # iterate rows, top-down
    for i in range(1, m + 1):
        # print(i), outputs 1 2 3 in columns
        
        # iterate columns, LR
        for j in range(1, n + 1):
            print(f'{j * i:^8}', end = '')
        
        # line break to make everything readable
        print()
    
from a05_aviation_calcs import calculate_ground_speed

def print_groundspeeds(va, course_dir):
    '''prints out groundspeeds using combinations of true air speed (mph) and course direction (degrees)'''
    
    # heading aspodifpOIJPoijfpSODIJFas jkf
    print('Windspeed and ground speed for a course direction')
    print(f'of {course_dir} degrees and a true airspeed of {va} mph:')
    print()
    print('wind speed -->    0             25          50          75         100')
    print(' wind dir        <-- ground speed (mph) -->')
    
    # iterate wind directions by top-down rows, assign to i
    
    for i in range(0, 360, 30):
        # print(f'{i:^8}') # outputs 0-330 in increments of 30
        print(f'{i:^9} ', end = '')
        
        # iterate wind speed columns as j IDK
        for j in range(0, 125, 25):
            
            # calculate_ground_speed(course_dir, va, wind_dir, vw)
            ground_speed = calculate_ground_speed(course_dir, va, i, j)
            print(f'{ground_speed:^13.1f}', end = '')
            
        print()

        
if __name__ == '__main__':
    
    print_products(3,5)
    # print_groundspeeds(200, 22.5)