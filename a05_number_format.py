# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 10:11:04 2023

@author: bayst
"""

# File: a05_number_format.py
# your name: Ding Xin
# your email: dmx@bu.edu
# U63555835
# CS108 A1

def format_date(month, day, year):
    '''returns YYYY-MM-DD'''
    
    # '02.0f' is used for months and days to put in 0's as placeholders     in front of single digit values
    
    return f'{year}-{month:02.0f}-{day:02.0f}'

def format_time(tm):
    'tm is inputted as minutes and floated'
    float(tm)
    
    # use integer div to separate hours and minutes
   
    hours = tm // 60
    
    # use modulus 60 to get the minutes, separate from hours, then integer div by 1 to get a whole number
    
    minutes = (tm % 60) // 1
    
    # modulus 1 gets us the partial minutes, which we then multiply by 60
    
    seconds = (tm % 1) * 60
    
    # use ':02.0f' to get rid of ".0's"
    return f'{hours:02.0f}:{minutes:02.0f}:{int(seconds):02.0f}'






if __name__ == '__main__':
    
    # test cases
    print('format_date(10, 9, 2002)', format_date(10, 9, 2002))
    print('format_date(3, 9, 2002)', format_date(3, 9, 2002))
    print('format_time(123.75)', format_time(123.75))
    print('format_time(0.5)', format_time(0.5))
    print('format_time(280)', format_time(280))