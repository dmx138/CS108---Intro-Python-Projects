# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 16:34:13 2023

@author: bayst
"""

# File: a11_string_accumulator.py
# your name: Ding Xin
# your email: dmx@bu.edu
# U63555835
# CS108 A1

def double(s):
    '''takes a string and doubles every character'''
    
    # define accumulator
    result = ''
    
    # use loop to process input
    for ch in s:
        
        # accumulate results
        result += 2 * ch
        
    # return accumulated results
    return result

def repeat_chars(s, n_times):
    '''takes a string and multiplies every ch by n_times'''
    
    # define accumulator
    result = ''
    
    # use loop to process input
    for ch in s:
        
        # accumulate results
        result += n_times * ch
    
    # return accumulated results
    return result

def num_vowels(s):
    '''returns the number of vowels in a given string'''
    
    # define accumulator
    # we use an integer count bc we're accumulating a numerical amount
    count = 0
    
    # use loop to process input
    for ch in s:
        
        # vowel detection
        if ch in ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'):
            # print(ch)
            
        # accumulate results
            count += 1 
    
    # return accumulated results
    return count
    
def double_vowels(s):
    '''processes a given string and doubles all vowels'''
    
    # define accumulator
    result = ''
    
    # use loop to process input
    for ch in s:
        
        # result += ch
        # vowel detection
        if ch not in ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'):
            # print(ch)
        # accumulate results
            result += ch
            
        else:
            result += ch * 2
        
    # return accumulated results
    return result 
    
def replace(s, old_ch, new_ch):
    '''processes a string, then replaces all letters assigned to old_ch with the new_ch'''
    
    # define accumulator
    result = ''
    
    # use loop to process input
    for ch in s:
    
        # accumulate results
        if ch == old_ch:
            result += new_ch
            
        else:
            result += ch
        
    # return accumulated results
    return result

def weave(s1, s2):
    '''takes two strings and uses a for loop to weave the two strings together in an alternating fashion'''
    
    
    # define accumulator
    result = '' 
    len_shorter = min(len(s1), len(s2)) 
    
    # use loop to process input
    
    # if s1 longer than s2
    if len(s1) > len(s2):
        
        longer_length = len(s1)
        # print('longer_length', longer_length)
        
        for i in range(len_shorter):
            
            # print(i) prints 0-6
            result += s1[i] + s2[i]
    
        # add any extras outside the loop so the extras don't get printed every loop
        result += s1[len_shorter:longer_length]
        
        # print(result)
        return result
    
    
    
    # if s2 longer than s1
    elif len(s2) > len(s1):
        
        longer_length = len(s2)
        
        for i in range(len_shorter):
            
            # print(i) prints 0-6
            result += s2[i] + s1[i]
            
        # add any extras outside the loop so the extras don't get printed every loop
        result += s2[len_shorter:longer_length]
        
        return result
            
    
    
    # if both strings are equal length
    if len(s1) == len(s2):
        for i in range(len_shorter):
            # print(i)
            result += s1[i] + s2[i]
            
        return result



if __name__ == '__main__':
    # print("double('hooray')", double('hooray'))
    # print("repeat_chars('ice cream!', 3)", repeat_chars('ice cream!', 3))
    # print("num_vowels('chocolate')", num_vowels('chocolate'))
    # print("double_vowels('COMPUTER SCIENCE')", double_vowels('COMPUTER SCIENCE'))
    # print("replace('hello, world!', 'l','w')", replace('hello, world!', 'l','w') )
    # print("replace('we love chocolate', 'o','a')", replace('we love chocolate', 'o','a'))
    # print("weave('chocolate', 'cookies')", weave('chocolate', 'cookies'))
    # print('weave("wwwwww", "aaaaaa")', weave("wwwwww", "aaaaaa"))
    print("weave('aaaaaa', 'bb')", weave('aaaaaa', 'bb'))