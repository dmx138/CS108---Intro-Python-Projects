# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 10:49:26 2023

@author: bayst
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 10:12:11 2023

@author: bayst
"""

# file: quiz3.py
# name: Ding Xin
# BUID: U63555835
# CS108 A1

def encode(s):
    '''returns a list of ASCII codes for a given string'''
    
    # accumulator for list
    result = []
    
    # iterate over each character in string
    for ch in s:
        # print(ch)
        
        result += [ord(ch)]
        
    return result
    
    
def count_upper_lower(phrase):
    '''procs a given string and returns a dictionary containing the counts of upper and lower case letters'''
    
    # 3 accumulators, one for upper and lower, and one for the dictionary
    result = {'lower': 0, 'upper': 0}
    # print(result['lower'])
    
    # iterate over each ch
    for ch in phrase:
        # print(ch)
        # print(result['lower'])
        # print(result['upper'])
            
        # lower cases
        if ord(ch) in range(97, 123):
            # print('yes')
            
            result['lower'] += 1
         
        # upper cases
        if ord(ch) in range(65, 91):
            # print('also')
            
            result['upper'] += 1
        
        # other characters ignored
        else:
            
            pass
            
    return result


class Temperature:
    '''creates a class that represents temperature with a value and scale F/C'''
    
    # initializes class attributes
    def __init__(self, value, scale):
        
        self.value = value
        self.scale = scale

    # def __copy__(self):
        
        
    # formats the class into a neat string representation
    def __repr__(self):

        return f'{self.value} {self.scale}'

    # converts to Celsius
    def value_in_c(self):
        
        if self.scale == 'C':
            
            return self.value
        
        elif self.scale == 'F':
            
            
            return (self.value - 32) * (5 / 9)
    
    # functions as our == operator, compares two values in CELSIUS
    def __eq__(self, other):
        
        if self.scale == 'F':
            
            self.value = (self.value - 32) * (5 / 9)
            
        if other.scale == 'F':
            
            other.value == (other.value - 32) * (5 / 9)
        
        return (self.value == other.value)
    
    
    
if __name__ == '__main__':
    # print(encode('goodbye'))
    # print(encode('thank you!'))
    phrase = "Through the Never"
    print(count_upper_lower(phrase))
    # t1 = Temperature(50, 'F')
    # t2 = Temperature(10, 'C')
    # t3 = Temperature(12, 'C')
    # print(t1)
    # # print(t2)
    # print(t1.value_in_c())
    # print(t1 == t2)
    # print(t1 == t3)