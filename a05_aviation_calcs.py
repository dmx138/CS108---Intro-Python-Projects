# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 10:50:21 2023

@author: bayst
"""

# File: a05_aviation_calcs.py
# your name: Ding Xin
# your email: dmx@bu.edu
# U63555835
# CS108 A1

import math
'''need math lololol'''

from a05_number_format import format_time

def calculate_heading(course_dir, va, wind_dir, vw):
    '''returns heading (angle in degrees) that a plane must travel, accounts for wind_direction and speed
    The paramaters are:
        the desired course direction of course_dir (degrees),
        the true airspeed of va (miles per hour),
        the direction of wind_dir (in degrees), and
        the wind speed of vw (miles per hour).
        
        heading = δ + ⍺ = delta + alpha = course + correction_angle
        alpha = math.asin((vw /va) * math.sin(wind_direction - course))
        
    Variables are:
        va - True airspeed – speed of the aircraft relative to the surrounding air;
        vw - Wind speed – speed of the wind relative to the ground;
        δ - Course – desired trajectory of the flight measured clockwise from the North;
        ω (wind_dir) - Wind direction – direction from which the air is blowing; and
        ⍺ - Wind correction angle – angle between the course and the heading (the direction to fly to compensate for the wind)'''
        
    # convert degrees to radians (test: success)
    course_dir_r = math.radians(course_dir)
    wind_dir_r = math.radians(wind_dir)
    # print('course_dir_r (heading) =', course_dir_r)
    # print('wind_dir_r (heading) =', wind_dir_r)
    
    # define parameter for sin (within asin)
    y = wind_dir_r - course_dir_r
    # print('y =', y)
    
    # define parameter for asin
    
    # x = float(math.radians(f'{(vw / va) * (math.sin(y)):.1f}')
    x = (vw /va) * math.sin(y)
    # x = (vw / va) * math.sin(o_theta - d_theta)
    # x = ((vw * math.sin(y)) / va)
    # print('x (heading) =', x)
    
    # alpha (wind correction angle, ⍺) calculation
    
    alpha = math.asin(x)
    # print('alpha (heading) =', alpha)
    
    # heading calc (δ + ⍺)
    
    heading_r = course_dir_r + alpha
    
    # convert back to degrees
    
    heading = math.degrees(heading_r)
    
    return heading

def calculate_ground_speed(course_dir, va, wind_dir, vw):
    '''calcs and returns groundspeed of plane given course direction and wind speed
    The paramaters are:
        the desired course direction of course_dir (degrees),
        the true airspeed of va (miles per hour),
        the direction of wind_dir (in degrees), and
        the wind speed of vw (miles per hour).
        
        vg = math.sqrt((va ** 2) + (vw ** 2) - (2 * va * vw * math.cos(course_dir - wind_dir + heading)))'''
        
        # have vg_squared = everything inside of sqrt fxn, then vg = math.sqrt(vg_squared)
        # keep track of what's in degrees (given parameters) and what's in radians (local variables) or else you WILL DIE
        
    '''The variables are:
        vg - Ground speed – aircraft’s speed relative to the ground;
        va - True airspeed – speed of the aircraft relative to the surrounding air;
        vw - Wind speed – speed of the wind relative to the ground;
        δ - Course – desired trajectory of the flight measured clockwise from the North;
        ω - Wind direction – direction from which the air is blowing; and
        ⍺ - Wind correction angle – angle between the course and the heading (the direction to fly to compensate for the wind)'''
        
    # convert to radians
    
    course_dir_r = math.radians(course_dir)
    wind_dir_r = math.radians(wind_dir)
    
    # print('course_dir_r (ground) =', course_dir_r)
    # print('wind_dir_r (ground) =', wind_dir_r)
    
    # assign alpha (use same eq from heading calc)
    
    y = wind_dir_r - course_dir_r
    x = (vw /va) * math.sin(y)
    alpha = math.asin(x)
    # print('alpha (ground) =', alpha)
    # print('y (ground) = ', y)
    # print('x (ground) = ', x)
    
    # # assign variable to parameter for cosine
    
    z = course_dir_r - wind_dir_r + alpha
    # print('z (ground) =', z)
    
    # create local var vg_squared, which is to be put inside math.sqrt
    
    vg_squared = (va ** 2) + (vw ** 2) - (2 * va * vw * math.cos(z))
    # print('vg_squared', vg_squared)
    
    # sqrt vg_squired
    
    vg = math.sqrt(vg_squared)
    
    return vg

def interactive_flight_planner():
    '''collects parameters used in calc fxns thru inputs'''
    
    print('Welcome to the interactive flight planner.')
    
    course_dir = float(input('Enter the course direction (in degrees): '))
    
    va = float(input('Enter the indicated air speed (in mph): '))
    
    wind_dir = float(input('Enter the wind direction (in degrees): '))
    
    vw = float(input('Enter the wind speed (in mph): '))
    
    heading = calculate_heading(course_dir, va, wind_dir, vw)
    
    ground_speed = calculate_ground_speed(course_dir, va, wind_dir, vw)
    
    distance = float(input('Enter your enroute distance (in miles): '))
    
    # miles / miles / hour, simplifies to hours
    e_time = float(distance / ground_speed)
    e_minutes = e_time * 60
    
    # conv to minutes, input into format_time
    enroute = format_time(e_minutes)
    print(enroute)
    
    # printerinos
    
    print('Here is a summary of your program inputs:')
    print('Course direction:', course_dir, f'degrees, air speed: {va:.0f} mph.')
    print('Wind direction:', wind_dir, f'degrees, wind speed: {vw:.0f} mph.')
    print()
    print('Given these parameters:')
    print('    Flying head:', heading, 'to stay on course.')
    print(f'    Ground speed will be: {ground_speed:.1f} mph')
    print()
    print('Enroute time is expected to be:', enroute)
    
if __name__ == '__main__':
    
    interactive_flight_planner()
    
    # le test cases
    # print('calculate_heading(90, 200, 90, 100)', calculate_heading(90, 200, 90, 100))
    # print('calculate_heading(90, 200, 270, 100)', calculate_heading(90, 200, 270, 100))
    # print('calculate_heading(90, 200, 180, 100)', calculate_heading(90, 200, 180, 100))
    # print('calculate_ground_speed(90, 200, 90, 100)', calculate_ground_speed(90, 200, 90, 100))
    # print('calculate_ground_speed(90, 200, 270, 100)', calculate_ground_speed(90, 200, 270, 100))
    # print('calculate_ground_speed(90, 200, 180, 100)', calculate_ground_speed(90, 200, 180, 100))