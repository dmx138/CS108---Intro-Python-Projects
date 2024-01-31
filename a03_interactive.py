# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 10:16:25 2023

@author: bayst
"""

# File: a03_interactive.py
# your name: Ding Xin
# your email: dmx@bu.edu
# U63555835
# CS108 A1

def username(first, middle, last):
    return first[0] + middle[0] + last[0:6]

def generate_username():
    print('Welcome to the user generated program. This program will generate your 8-character username')
    
    last = input('Enter your last name: ')
    
    first = input('Enter your first name: ')
    
    middle = input('Enter your middle name: ')
    
    print('Welcome, ', first + ' ' + middle + ' ' + last + '.')

    print('Your username is: ', username(first, middle, last))
    
if __name__ == '__main__':
    
    generate_username()