# -*- coding: utf-8 -*-
"""
Created on Sat Oct  7 19:33:36 2023

@author: bayst
"""

# File: a10_indefinite_loop.py
# your name: Ding Xin
# your email: dmx@bu.edu
# U63555835
# CS108 A1

import random

def print_bugs_in_the_code():
    '''prints out the bugs in the code song IDK'''
    bugs = random.randint(1, 100)
    
    print(f'{bugs} little bugs in my code,')
    print(f'{bugs} little bugs!')
    print('take one down, patch it around...')
    
    # create new bugs
    
    bugs = random.randint(1, 100)
    print(f'{bugs} little bugs in my code!')
    print()
    
    # normal scenarios
    while bugs != 42:
        print(f'{bugs} little bugs in my code,')
        print(f'{bugs} little bugs!')
        print('take one down, patch it around...')
        
        bugs = random.randint(1, 100)
        print(f'{bugs} little bugs in my code!')
        print()
        
    
    # when bugs = 42
    if bugs == 42:
        print(f'{bugs} little bugs in my code...')
        print("Good enough, it's time for beers!")
    
def check_age():
    '''interactive that checks if you are old enough to drink'''
    age = int(input('What is your age? '))
    
    # set condition if underaged
    while age < 21:
        print('Bzzt! You are not old enough to drink.')
        
        # asking for age again continues the loop, no need to recall the function within fxn
        age = int(input('What is your age? '))
        
    # when the condition is met
    
    if age >= 21:
            print('Okay! You are old enough')
        
def guess_your_number():
    '''interactive that guesses users number'''
    print('This program will guess your number in as few guesses as possible.')
    
    # set lower and higher bounds
    lower_bound = int(input('Enter a lower bound: '))
    higher_bound = int(input('Enter a higher bound: '))
    
    # initial guess
    guess = higher_bound // 2
    print(f'Our guess is {guess}')
    
    # # set higher_bound to guess for later use
    # higher_bound = guess
    
    # set up variable to accumulate # of guesses
    count = 1
    
    # collect user response, if correct (c), stop. if too high or low (h/l), keep going
    response = input('Is that correct (c), too high (h) or too low (l)? ')
    
    # incorrect response
    while response != 'c':
        
    # if response is too high (h)
        if response == 'h':
            
            # shift the upper bound to our previous guess, bc it was too high
            higher_bound = guess
            guess = (lower_bound + higher_bound) // 2
            print(f'Our guess is {guess}')
            
            # collect guess count thru loops
            count += 1
            
            # continues the loop and guessing game
            response = input('Is that correct (c), too high (h) or too low (l)? ')
    
    # if response is too low (l)
        if response == 'l':
            
            # set lower bound to previous guess, bc it was too low
            lower_bound = guess
            guess = (lower_bound + higher_bound) // 2
            print(f'Our guess is {guess}')
            
            # collect guess count thru loops
            count += 1
            
            # continues the loop and guessing game
            response = input('Is that correct (c), too high (h) or too low (l)? ')
            
    # guess is correct, loop ends and count is accumulated
    if response == 'c':
        print(f'It took {count} tries to guess your number is {guess}')
        
if __name__ == '__main__':
    # print_bugs_in_the_code()
    check_age()
    # guess_your_number()