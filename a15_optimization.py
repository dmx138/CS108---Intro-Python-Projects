# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 11:35:57 2023

@author: bayst
"""

# File: a15_optimization.py
# your name: Ding Xin
# your email: dmx@bu.edu
# U63555835
# CS108 A1

def longest_word(words):
    '''iterates a list and returns the longest word in the list'''
    
    scored_list = [[len(w), w] for w in words]
    
    result = max(scored_list)
    
    return result[1]
    
    
from a15_list_comprehensions import factors

def most_factors(numbers):   
    '''returns the integer with the most factors within a list'''
    
    scored_list = [[len(factors(i)), i] for i in numbers]
    # print(scored_list)
    
    result = max(scored_list)
    
    return result[1]


from a15_list_comprehensions import num_vowels

def most_vowels(phrase):
    '''procs a phrase and returns the wrod with the most vowels'''

    scored_list = [[num_vowels(w), w] for w in phrase.split()]
    # print(scored_list)

    result = max(scored_list)
    
    return result[1]





if __name__ == '__main__':
    words = ['running', 'down', 'a', 'dream']
    print(longest_word(words))
    # print(most_factors([5,10,16,20,25]))
    # phrase = "I'm learning to fly But I ain't got wings Coming down Is the hardest thing"
    phrase = "That's right, nothing else can change my world."
    print(most_vowels(phrase))