# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 00:50:57 2023

@author: bayst
"""

# File: a06_find_min.py
# your name: Ding Xin
# your email: dmx@bu.edu
# U63555835
# CS108 A1

def my_min(a, b):
    '''determines and returns the smaller value between 2 given parameters'''
    if a < b:
        m = a
        
    else:
        m = b

    # m stands for minimum
    
    return m
        
def find_min(a, b, c):
    '''determines and returns the smallest value out of a set of 3 given parameters'''
        
    if a < b and a < c:
        m = a
        
    else:
        m = b
    
        if m < c:
            m = b
            
        else: 
            m = c
            
    return m
        
        
if __name__ == '__main__':
    # print('my_min(1,2)', my_min(1,2))
    # print('my_min(2,1)', my_min(2,1))
    # print('my_min(46,138)', my_min(46,138))
    # print('find_min(2, 1, 3)', find_min(2, 1, 3))
    # print('find_min(1, 2, 3)', find_min(1, 2, 3))
    # print('find_min(3, 2, 1)', find_min(3, 2, 1))
    print('find_min(1, 1, 2)', find_min(1, 1, 2))
    print('find_min(2, 1, 1)', find_min(2, 1, 1))
    print('find_min(1, 2, 1)', find_min(1, 2, 1))
    print('find_min(2, 1, 2)', find_min(2, 1, 2))
    