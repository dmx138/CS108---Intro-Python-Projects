# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 23:15:14 2023

@author: bayst
"""

# File: a11_guessing_game.py
# your name: Ding Xin
# your email: dmx@bu.edu
# U63555835
# CS108 A1

def process_guess(secret_word, revealed_word, guess):
    '''processes guesses for a hangman-like word guessing game'''
    result = ''
           
    # ONE AT A TIME 
    # def loop to accumulate string
    for i in range(len(secret_word)): # allows us to process every space in the secret word
        # print(i) # 0 1 2 3 4
        
        # accumulates a letter if there's already a useful word in revealed_word
        if revealed_word[i] == secret_word[i]:
           
            result += revealed_word[i]
           
        # accumulates a letter if the guess is correct 
        if guess == secret_word[i]:
           
            result += guess
           
        # if the other 2 conditions aren't met, then a '-' is accumulated
        if guess != secret_word[i] and revealed_word[i] != secret_word[i]:
           
            result += '_'
    
     # print(result)
    return result

def guess_my_word(secret_word, chances = 3):
    '''the rest of game lies here, with a given amount of chances'''
    
    
    # (a) setup, 2 accumulators
    revealed_word = '_' * len(secret_word)
    # print(revealed_word)
    incorrect_guesses = 0
    # print(incorrect_guesses)
    wrong_guesses = ''
    
    # (b) game loop, indefinite until player wins or loses
    # win: revealed_word == secret_word
    # lose: incorrect_guesses = chances
    
    # need two conditions for the indefinite loop to continue because we have two stop conditions
    while incorrect_guesses != chances and revealed_word != secret_word:
        
        print('Try to guess the secret word; you have 3 incorrect guesses remaining.')
        print(f'Your clues: {revealed_word}')
        print(f'Incorrect guesses: {incorrect_guesses}')
        print()
        guess = input('Guess a letter: ')
        
        if guess in secret_word: # hmmmm
        
            # print(process_guess(secret_word, revealed_word, guess))
            
            revealed_word = process_guess(secret_word, revealed_word, guess)
            
            print(f'Try to guess the secret word; you have {chances - incorrect_guesses} incorrect guesses remaining.')
            print(f'your clues: {revealed_word}')
            print(f'Incorrect guesses: {incorrect_guesses}')
            print()
            
            # don't need this, new guess collected at line 66
            # guess = input('Guess a letter: ')
            
        else:
            
            incorrect_guesses += 1
            wrong_guesses += guess + ' '
            print(f"The letter '{guess}' does not appear in the secret word")
            print(f'Try to guess the secret word; you have {chances - incorrect_guesses} incorrect guesses remaining.')
            print(f'Your clues: {revealed_word}')
            print(f'Incorrect guesses: {wrong_guesses}')
            print()
    
    # win scenario
    if revealed_word == secret_word: 
        
        print('You got it! YIPPEEEE!')
        print(f'The secret word was: {secret_word}')
        
    
    # lose scenario
    if incorrect_guesses == chances:
        
        print(f'Incorrect! The letter {guess} does not appear in the secret word.')
        print('You lose.')
        print(f'The secret word was: {secret_word}')
        
    # (c) processing guesses
    
        # guess = input('Guess a latter: ')
    # (d) revisions
            

if __name__ == '__main__':
    # process_guess('apple', '-----', 'a') #1
    # process_guess('apple', '-----', 'p') #2
    # process_guess('apple', 'a----', 'e') #3 figure out how to keep already solved letters
    # process_guess('apple', 'a---e', 'p') #4
    # print("process_guess('apple', 'a---e', 'p')", process_guess('apple', 'a---e', 'p'))
    # print(process_guess('programming', 'p----------', 'r'))
    
    # guess_my_word('programming')
    guess_my_word('pneumonoultramicroscopicsilicovolcanoconiosis')