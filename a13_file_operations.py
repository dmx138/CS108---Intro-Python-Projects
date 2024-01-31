# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 10:40:49 2023

@author: bayst
"""

# File: a13_file_operations.py
# your name: Ding Xin
# your email: dmx@bu.edu
# U63555835
# CS108 A1

def grep(pattern, filename):
    '''searches for and returns all instances of the pattern in the file, filename'''
    
    file = open(filename, 'r')
    # print(f)
    
    result = ''
        
    for line in file:
        
        if pattern in line:
            
            result += line
            
    file.close()
    
    return result

def grep_count(pattern, filename):
    '''counts the number of lines containing the pattern within a txt file'''
    
    file = open(filename, 'r')
    
    result = 0
    
    for line in file:
        
        if pattern in line:
            
            result += 1
        
    file.close()
    
    return result

def find_and_replace(input_filename, out_filename, old_pattern, new_pattern):
    '''input_filename identifies and processes a string by finding a pattern and replacing it with a new pattern'''
    
    file = open(input_filename, "r") # read, write, or append?
    print(f"Read input file '{input_filename}'.")        
    
    fn = open(out_filename, 'w')
    
    text = file.read()
    
    # new_text = ''
    
        
    if old_pattern.lower() in text:
            
        # replace lowercase patterns
        new_text = text.replace(old_pattern.lower(), new_pattern.lower())
        
            
    if old_pattern.upper() in text:
            
        # replace UPPERCASE patterns
        new_text = new_text.replace(old_pattern.upper(), new_pattern.upper())
            
            
    if old_pattern.title() in text:
    
        # replace Title 
        new_text = new_text.replace(old_pattern.title(), new_pattern.title())
            
    # print(new_text) this works
        
    fn.write(new_text)
        # print(text)
    
    file.close()
    fn.close()
    
    # count for the default scenario
    default_occurences = text.count(old_pattern)
    
    if default_occurences > 0:
        
        print(f"Replaced {default_occurences} occurences of `{old_pattern}` with `{new_pattern}`")
    
    else:
        
        print(f"No occurences of `{old_pattern}` were found")
    
    
    # counter number of times titles are replaced
    title_occurences = text.count(old_pattern.title())
    
    # title printouts
    if title_occurences > 0:

        print(f"Replaced {title_occurences} occurences of `{old_pattern.title()}` with `{new_pattern.title()}`")

    else:

        print(f"No occurences of `{old_pattern.title()}` were found")
        
        
    # count number of times lower is replaced
    lower_occurences = text.count(old_pattern.lower())

    # lower printouts
    if lower_occurences > 0:
        
        print(f"Replaced {lower_occurences} occurences of `{old_pattern.lower()}` with `{new_pattern.lower()}`")
        
    else:
        
        print(f"No occurences of `{old_pattern.lower()}` were found")
    
    
    # count number of times upper is replaced
    upper_occurences = text.count(old_pattern.upper())
    
    # upper printouts
    if upper_occurences > 0:
        
        print(f"Replaced {upper_occurences} occurences of `{old_pattern.upper()}` with `{new_pattern.upper()}`")
        
    else:
        
        print(f"No occurences of `{old_pattern.upper()}` were found")
    
    
    print(f"Wrote output file '{out_filename}'")



if __name__ == '__main__':
    # print(grep('time', 'time.txt'))
    # print(grep_count('time', 'time.txt'))
    print(find_and_replace('all_you_need.txt', 'all_you_need_out.txt', "Love", "Chocolate"))
    # print(find_and_replace('romeo.txt', 'romeo_out.txt', "love", "chocolate"))