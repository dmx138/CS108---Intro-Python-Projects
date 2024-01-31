# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 17:32:24 2023

@author: bayst
"""

# File: a14_list_of_strings.py
# your name: Ding Xin
# your email: dmx@bu.edu
# U63555835
# CS108 A1

def print_word_lengths(words):
    '''procs a list with strings and returns each word along with its length'''
    
    for s in words:
        
        # to be concatenated into the f-string
        length = len(s)
        
        print(f'{s} {length}')


def concatenate(words, separator = ' '):
    '''procs a string list and returns a big string with all substrings concatenated, optional separator'''
    
    # accumulator variable to be returned later
    result = ''
    
    # iterate each list string for the printout
    for s in words:
        
        
        # cut off the separator at the end
        if s == words[(len(words) - 1)]:
            
            result += s
        
        # every other character we add the separator after
        else:
            
            result += s + separator
            
    return result
    

def change_case(s):
    '''procs a string and reverses the capitalization of each word'''
    
    # accumulator
    result = ''
    
    # convert the string into a list to iterate each word
    for w in s.split():
        # print(w, end = '')
        
        # if 'a' <= w <= 'z' or 'A' <= w <= 'Z':
        #     print(w)
        
        # print(ord(w))
        # upper to lower
        if w == w.upper():
            
            result += w.lower() + ' '
            
        # lower to upper
        if w == w.lower():
            
            result += w.upper() + ' '
            
    return result[:-1]
            
        # account for non-letters
        # if ord(w) < 65 or 90 < ord(w) < 97 or ord(w) > 122:
            
        #     print(w, end = '')
    
    


if __name__ == '__main__':
    words = ['The', 'long', 'and', 'winding', 'road']
    # print_word_lengths(words)
    # print(concatenate(words))
    # print(concatenate(words, ', '))
    s = 'aa BB cc DD AA'
    print(change_case(s))