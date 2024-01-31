# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 10:44:22 2023

@author: bayst
"""

# File: a07_printing_shapes.py
# your name: Ding Xin
# your email: dmx@bu.edu
# U63555835
# CS108 A1

def print_rect(ch, width, height):
    '''prints out ch in the shape of rectangle with dimensions width and height'''
    # our parameter for range controls verticality
    for i in range(height):
    
        # printing ch * width controls horizontal width
        print(ch * width)

def print_lower_left_triangle(ch, height):
    '''prints out ch in the shape of triangle with 90 degree corner in the lower left'''
    # we are controlling how many times to repeat ch with loop counter variable
    for i in range(height):
        
        # print(i) gives a column of 1 ch's
        # multiplying ch by i makes every line short of 1 ch, so add 1
        print(ch * (i + 1))
        
def print_upper_left_triangle(ch, height):
    '''prints out ch in the shape of triangle with 90 degree corner in upper left'''
    # putting in 0 and -1 reverses the i in height printout
    for i in range(height, 0, -1):
        
        # because our stop parameter is 0, 0 isn't included so we don't have to put i + 1, just i
        print(ch * i)
    
def print_lower_right_triangle(ch, height):
    '''prints out ch in the shape of triangle with 90 degree corner in lower right'''
    # reverse the i printout again
    for i in range(height, 0, -1):
        # print((' ' * (i -1)) + (ch * (6 - i)))

        print(' ' * (i - 1) + (ch * ((int(height) + 1)  - i)))
        
def print_upper_right_triangle(ch, height):
    '''prints out ch in the shape of triangle with 90 degree corner in upper right'''
    for i in range(height, 0, -1):
    # for i in range(0, height):    
        # same idea, spaces and ch = 5, pattern is just reversed
        print((' ' * (int(height) - i)) + (ch * i))
        # print(i)
        # print(' ' * ((ch * int(height))
        
def print_pyramid(ch, height):
    '''prints out ch in the shape of a pyramid'''
    for i in range(height):
        # print(i)
    
        spaces = ' ' * (int(height - 1) - i)
        char = (ch * (2 * (i + 1) - 1)) 
        
        print(f'{spaces}{char}')
        
def print_diamond(ch, height):
    '''prints ch in the shape of a diamond'''
    # let's try splitting this up, start by building pyramid
    pyramid = height // 2
    for i in range(pyramid):
        # print(i): 0, 1, 2, 3, 4
        # this pyramid is largely the same, but because the range is larger, i int div by 2
        spaces = ' ' * (int((height // 2) - 1)- i)
        char = (ch * (2 * (i + 1) - 1))
        
        print(f'{spaces}{char}')
        
    # now do the other half
    for i in range(pyramid - 1, 0, -1):
        # print(i), output: 4, 3, 2, 1
        # (height // 2) - 1 reverses the order of print(i), allowing us to simply multiply it by ' '
        spaces2 = ' ' * ((height // 2) - i)
        char2 = (ch * ((2 * i) - 1))
        
        print(f'{spaces2}{char2}')
        
        

# problem 4: there are spaces to the left of ch, the # of spaces and ch add up to 5 (height) per row
if __name__ == '__main__':
    # print('print_rect(*, 7, 5)', print_rect('*', 7, 5))
    # print('print_lower_left_triangle(*, 5)', print_lower_left_triangle('*', 5))
    # print('print_upper_left_triangle(*, 5)', print_upper_left_triangle('*', 5))
    # print('print_lower_right_triangle(*, 5)', print_lower_right_triangle('*', 5))
    # print('print_upper_right_triangle(*, 5)', print_upper_right_triangle('*', 5))
    # print('print_pyramid(*,5)', print_pyramid('*',5))
    print('print_diamond(*,10)', print_diamond('*',10))