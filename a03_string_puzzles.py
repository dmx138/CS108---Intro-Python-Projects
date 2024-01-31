# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 13:39:58 2023

@author: bayst
"""

# File: a03_string_puzzles.py
# your name: Ding Xin
# your email: dmx@bu.edu
# U63555835
# CS108 A1

def full_name(first_name, last_name):
    """returns full name"""
    Firstname = first_name
    Lastname = last_name
    return Lastname + ", " + Firstname

def initials_only(first_name, last_name):
    """returns initials of first and last name"""
    F = first_name[0]
    L = last_name[0]
    return F + L

def truncate(s, max_length):
    """slices full name starting from the first letter to a given max length"""
    print(type(max_length))
    return s[0:max_length]

def swap_halves(s):
    """identifies and splits full name and swaps halves"""
    length = len(s)
    halfway = (len(s)) // 2
    first_half = s[0:halfway]
    last_half = s[halfway:length]
    return last_half + first_half

def outside_chars(s, n):
    """splices first and last characters to the nth position and returns the combined results"""
    return s[0:n] + s[((len(s)) - n):(len(s))]
    
def slice_middle(s):
    """indentifies middle half of full name and returns it"""
    first_quarter = len(s) // 4
    middle = len(s) // 2
    third_quarter = first_quarter + middle
    return s[first_quarter:middle] + s[middle:third_quarter]

def triple_outsides(s):
    """returns full name but with the first and last characters tripled"""
    return (s[0] * 2) + s + ((s[len(s) - 1] * 2))
    
def every_other(s):
    """returns full name but with every other character"""
    return s[0:(len(s)): 2]

def reverse(s):
    """reverses full name"""
    return s[(len(s) - 1): :-1]

def rotate(s, n):
    """shifts every character in full name 2 positions to the left"""
    first_two = s[0:n]
    the_rest = s[n: ]
    return the_rest + first_two
        
if __name__ == '__main__':

    # variables to test functions
    first_name = 'Ding'
    last_name = 'Xin'
    s = "Ding Xin"
    max_length = 6
    n = 2
    
    # prints
    print(full_name(first_name, last_name))
    print(initials_only(first_name, last_name))
    print(truncate(s, max_length))
    print(swap_halves(s))
    print(outside_chars(s, n))
    print(slice_middle(s))
    print(triple_outsides(s))
    print(every_other(s))
    print(reverse(s))
    print(rotate(s, n))
    