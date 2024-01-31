# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 00:19:19 2023

@author: bayst
"""

# File: s13_strings.py
# your name: Ding Xin
# your email: dmx@bu.edu
# U63555835
# CS108 A1

# some strings to work with:
s1 = 'Three little kittens lost their mittens'	
s2 = 'Star light, star bright'
s3 = 'Nothing YOU can do, but YOU can learn how to be YOU in time'

# s1.title() capitalizes the first letter of each word

def to_upper_case(s, word):
    '''takes a string and capitalizes all occurences of word'''
    # print(s1)
    
    # uppercase all instances of the fully lower cased word
    lowered_replaced = s.replace(word, word.upper())
    
    
    
    # now we account for all titled instances of word
    # print(word.title())
    title_replaced = lowered_replaced.replace(word.title(), word.upper())
    
    return title_replaced
    
    
    
def count_vowels(s):
    '''counts the amount of all vowels in the string'''
    
    count = 0
    
    # lowered_string = s.lower()
    
    # count smol vowels
    count += s.count('a') + s.count('e') + s.count('i') + s.count('o') + s.count('u') 
    
    # count big vowels, split into two lines for readability
    count += s.count('A') + s.count('E') + s.count('I') + s.count('O') + s.count('U')
    
    
    return count
    
    
    
if __name__ == '__main__':
    # to_upper_case(s1, 'little')
    # to_upper_case(s1, 'tt')
    # to_upper_case(s2, 'star')
    # print(to_upper_case('One Fish two fish red fish blue fish', 'fish'))
    # count_vowels(s1)
    print(count_vowels(s3))