# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 02:46:14 2023

@author: bayst
"""

# File: a12_caesarcipher.py
# your name: Ding Xin
# your email: dmx@bu.edu
# U63555835
# CS108 A1

def shift_char(c, n):
    '''shifts character "c" by n spaces in ASCII'''
    # ord(''): letter -> number
    # chr(): number -> letter
    
    # tests for lowercase (bounds are 97-122)
    if 'a' <= c <= 'z':
        
        chr_result = ord(c) 
        # print(chr_result)
        cipher_shift = chr_result + n
        # print(caesar_cipher)
        # print(chr(cipher_shift))
        
        # normal scenario
        if cipher_shift >= 97 and cipher_shift <= 122:
            
        #     # print(chr(caesar_cipher))
            return chr(cipher_shift)

    
    
        # if we need to wrap c around the alphabet back to front
        if cipher_shift > 122:
            
            back_wrap_around = cipher_shift - 26
            # print(wrap_around) # test case with x gives 97 (a)
            
            return chr(back_wrap_around)
        
        # if we need to wrap c around the alphabet front to back
        if cipher_shift < 97:
            
            front_wrap_around = cipher_shift + 26
            # print(front_wrap_around) # test case with a, -2 gives 121 (y)
    
            return chr(front_wrap_around)
        
        
        
    # test for uppercase, bounds have to be diff than lowercase (65-90)
    if 'A' <= c <= 'Z':
        
        chr_result = ord(c) 
        # print(chr_result)
        cipher_shift = chr_result + n
        # print(caesar_cipher)
        # print(chr(cipher_shift))
        
        # normal scenario
        if cipher_shift >= 65 and cipher_shift <= 90:
            
        #     # print(chr(caesar_cipher))
            return chr(cipher_shift)

    
    
        # if we need to wrap c around the alphabet back to front
        if cipher_shift > 90:
            
            back_wrap_around = cipher_shift - 26
            # print(wrap_around) # test case with x gives 97 (a)
            
            return chr(back_wrap_around)
        
        # if we need to wrap c around the alphabet front to back
        if cipher_shift < 65:
            
            front_wrap_around = cipher_shift + 26
            # print(front_wrap_around) # test case with a, -2 gives 121 (y)
    
            return chr(front_wrap_around)
    
    
    # dont't shift non-letters!
    if ord(c) not in range(65, 90) or ord(c) not in range(97, 122):
        
        return c
    
    
    
def cipher(plaintext, n):
    '''encrypts a string using the shift_char fxn'''
    
    # accumulator variable
    ciphertext = '' 
    
    for i in plaintext:
        # print(i)
        
        encrypted_text = shift_char(i, n)
        # print(encrypted_text)
        
        ciphertext += encrypted_text
        
    # print(ciphertext)
    return ciphertext
        

def codebreaker(ciphertext):
    '''uses ciphertext from the above cipher fxn and decodes it with 26 shifts 
    one of the results is coherent English'''
    
    for i in range(1, 27):
        # print(i)
        
        cipher(ciphertext, i)
        
        
        print(cipher(ciphertext, i))
    
    
if __name__ == '__main__':
    # shift_char('a',3)  # simple case: no wrap around needed'd'
    # shift_char('x',3)  # wrap around the end of the alphabet'a'
    # shift_char('z',3)
    # shift_char('a',-2) # wrap around the beginning of the alphabet'y'
    # shift_char('A', 3) # no wrap around -> 'D'
    # shift_char('X', 3) # wrap around the end -> 'A'
    # shift_char('A', -2) # wrap aroundt the front end -> 'Y'
    # shift_char(' ', 5)
    # shift_char('!', 2)
    # cipher('time', 4) # returns 'xmqi'
    print(cipher('welcome to the machine', 19)) # returns 'pxevhfx mh max ftvabgx'
    # cipher('yOUr SoUL is mInE', 3) # returns 'bRXu VrXO lv pLqH'
    # codebreaker('xmqi')
    # codebreaker('pxevhfx mh max ftvabgx')
    # codebreaker('bRXu VrXO lv pLqH')
    # codebreaker('FEROEM')
    # codebreaker('ivwo wvoidks max sjdefdf')