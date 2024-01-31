# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 23:27:05 2023

@author: bayst
"""

# File: a17_decipher.py
# your name: Ding Xin
# your email: dmx@bu.edu
# U63555835
# CS108 A1

from a12_caesarcipher import cipher
from a16_dict_operations import letter_frequencies

def englishness_score(s, frequencies):
    '''calcs and returns a floating score that descibres the Englishness (wtf) of a string, the higher the score the more English it is'''
    
    # dictionary d has the frequences based on the quick brown fox text
    # print(d)
    # print()
    
    
    # accumulator variable 
    englishness = 1
    
    # print('frequencies', frequencies)
    
    # iterate the string over each character
    for ch in s:
        
    
        # print(d[ch])
        
        # accumulate by multiplying
        if ord(ch) in range(97, 123):
            
            englishness = englishness * frequencies[ch]
            
            # print(d[ch])
        # if non letters
        else:
            
            pass
        
        
    # return accumulator
    return englishness
    


def decipher(s, frequencies):
    '''decrypts a caesar cipher encrypted string using letter frequencies and returns plaintext string'''
    
    # create a list of options with all 26 cipher permutations of string s
    options = [cipher(s, i) for i in range(1, 27)]
    # print(options)
    
    
    # created a list of scored options that contains the english score for all permutations
    scored_options = [(englishness_score(s, frequencies), s) for s in options]
    # print(scored_options)
    
    
    # use built in max fxn to find the most english string 
    high_score = max(scored_options)
    # print(high_score)
    
    
    # return just the string
    return high_score[1]


if __name__ == '__main__':

    # here is some sample text, which contains all 26 letters
    # but is not fully representative of the English language
    # text = 'the quick brown fox jumps over the lazy dog' 
    # d = letter_frequencies(text)
    # print("englishness_score('uryyb, jbeyq!', d)", englishness_score('uryyb, jbeyq!', d))
    # print("englishness_score('hello, world!', d)", englishness_score('hello, world!', d))
    # s1 = 'jsv alsq xli fipp xsppw'
    # s2 = 'for whom the bell tolls'
    # print("englishness_score(s1, d)", englishness_score(s1, d))
    # print("englishness_score(s2, d)", englishness_score(s2, d))
    f = open('romeo.txt')
    text = f.read()
    f.close()
    d = letter_frequencies(text)
    s1 = 'h svun aptl h nv pu h nhshef mhy mhy hdhf'
    print(decipher(s1, d))