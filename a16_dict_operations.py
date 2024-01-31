# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 10:15:17 2023

@author: bayst
"""

# File: a16_dict_operations.py
# your name: Ding Xin
# your email: dmx@bu.edu
# U63555835
# CS108 A1


def print_dict(d):
    '''procs a dict and prints out all key + value pairs'''
    
    # print(type(list(d))) # lists parameter d
    # sort a list of d
    key_list = list(d.keys())
    # key_list 
    # print(d[1]) # no
    
    key_list.sort()
    
    # print(key_list)
    
    # iterate over all keys in d
    for keys in key_list:
        # print(keys) # prints out schools
        # print(d[keys]) # prints out numbers
        # print(d[keys].sort())
        
        # d[keys].sort()
        
        print(f'{keys}: {d[keys]}')


def scrabble_score(word):
    '''procs a string and returns its scrabble score'''
    
    # accumulator for the scrabble score
    score = 0
    
    # dict of letters and scrabble points
    letter_scores = {'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 
   'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 
   'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10}
    # print(type(letter_scores))
    
    # iterate over each letter in the word
    for l in word:
        # print(l)
        
        # account for upper case letters
        l = l.lower()
        
        
        # accumulate each letter's scrabble score
        # print(letter_scores[l])
        score += letter_scores[l]
        
        # print(type(l.upper))
        
        
    return score
            

def best_word(words):
    '''procs a list of words and uses the scrabble_score fxn to return the word with the highest scrabble score'''
    
    # use list comprehension to create a list of the words
    scored_list = [[scrabble_score(w), w] for w in words]
    print(scored_list)
    
    winner = max(scored_list)
    # print(winner)
    
    return winner[1]


def letter_counts(text):
    '''procs text and returns a dict of each letter and the number of times they occur'''
    
    # swag method to define d
    d = dict([[chr(x), 0] for x in range(97, 123)])
    # print(d)

        
    # iterate over each ch in text
    for ch in text:
        
        # accounts for non letters
        if ch in d: 
            
            # accounts for uppercases
            ch = ch.lower()
            
            # print(d[ch])
            # accumulate the count in the dict
            d[ch] += 1
        
        
    return d
    
        
def letter_frequencies(text):
    '''procs text and returns relative frequences of a ll letters in the text'''
    
    # print(type(letter_counts(text))) # running the countx fxn returns a dict
    d = letter_counts(text)
    # print(d)
    
    # acquire le count for relative frequency
    # use an accumulator because it makes more sense
    count = 0
    
    # iterate over the original dictionary
    for ch in d:
        
        # print(d[ch])
        
        # simply accumulate d[ch], which is the numerical value
        count += d[ch]
        # print(count)
    
    
    d = dict([[ch, d[ch] / count] for ch in d])
    
    return d
            
        



if __name__ == '__main__':
    d1 = {'BU': 5, 'BC':3, 'Harvard':4, 'Northeastern':1} # alpha keys
    d2 = {8:5, 2:7, 3:4, 9:2, 5:13} # numeric keys
    # print_dict(d2)
    # print_dict(d2)
    # print(scrabble_score('jubilant'))
    # print(scrabble_score('JUBILANT'))
    # print(scrabble_score('pneumonoultramicroscopicvolcanoconiosis'))
    words = ['nitwit', 'blubber', 'oddment', 'tweak']
    print(best_word(words))
    # print(letter_counts('testing 1 2 3!'))
    # print(letter_frequencies('hello, world'))