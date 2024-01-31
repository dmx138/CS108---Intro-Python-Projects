# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 11:26:45 2023

@author: bayst
"""

# File: a17_markov.py
# your name: Ding Xin
# your email: dmx@bu.edu
# U63555835
# CS108 A1

import random

def create_markov_model(text):
    '''procs a string and returns a dictionary of a word and possible words that may come next based on the given text'''
    
    # split text into a list of words
    word_list = text.split()
    # print(word_list)
    
    
    # accumulator variable for a dictionary
    d = {}
    
    
    # establish current word as '$'
    current_word = '$'
    d[current_word] = []
    
    
    # iterate each word in word list
    for next_word in word_list:
        
        
        # if the iterated word isn't already in the dictionary, establish it as a new key
        if current_word not in d:
            
            d[current_word] = [next_word]
        
        # if the iterated word is already in the dictionary, establish the next word as a key value
        else:
            
            d[current_word] += [next_word]
    
        # update current word to be either next_word or '$'
        if next_word[-1] in ('!', '?', '.'):
            
            current_word = '$'
            
        else:
            
            current_word = next_word
        
        
    return d
    
    
def generate_markov_text(model, num_words):
    '''takes a dictionary of word transitions created by the previous fxn and accumulates a string based on this dictionary'''
    
    # print(model)
    
    # accumulator for the text
    markov_text = ''
    
    # start with '$' as it is a sentence starter
    current_word = '$'
    
    
    for i in range(num_words):
        # print(i)
        
        # the following values after the current word should include the key values of the current word
        following_words = model[current_word]
        # print(following_words)
        
        # the next word will then include a random choice from following_words
        next_word = random.choice(following_words)
        
        
        # accumulate the next word into accumulator
        markov_text += next_word + ' '
        
        
        # assign current word to either next_word or '$'
        if next_word[-1] in ('!', '?', '.'):
            
            current_word = '$'
            
        else:
            
            current_word = next_word
            
            
    return markov_text
        
        
    
    
if __name__ == '__main__':
    # text = 'A B A. A B C. B A C. C C C.'
    filename = 'romeo.txt'
    f = open(filename)
    text = f.read() # read entire file as one string
    # text = ""
    model = create_markov_model(text) # output: {'A': ['B', 'B', 'C.'], 'C': ['C', 'C.'], B': ['A.', 'C.', 'A'], '$': ['A', 'A', 'B', 'C']}
    # print(model)
    # print(generate_markov_text(model, 20))
    print(generate_markov_text(model, 50))