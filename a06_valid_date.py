# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 01:23:03 2023

@author: bayst
"""

# File: a06_valid_date.py
# your name: Ding Xin
# your email: dmx@bu.edu
# U63555835
# CS108 A1

def is_valid_month(month):
    '''determines if a given month number is valid or not (0-12) and returns T/F accordingly'''
    if month > 0 and month <= 12:
        return True
    
    else:
        return False

def is_leap_year(year):
    '''determines if a given year is T/F
    LY conditions:
        - Any year divisible by 400 is a leap year. (e.g., 2000, 2400)
        - Other centuries are not leap years (e.g., 2100 is not a leap year)
        - Other years divisible by 4 are leap years (e.g., 2020, 2024)
        - All other years are not leap years.'''
    
    # Any year divisible by 400 is a leap year. Years 138000 and 9100 will be tested.
    
    if (year % 400) == 0:
        return True
    
    # Other years divisible by 4 are leap years
        
    elif (year % 4) == 0:
        return True
        
    else:
        return False
    
def is_valid_day_in_month(month, day, year):
    '''determines if a day number is valid given a certain month/leap year'''
    # 2 nested ifs at most
    
    # check if month is a 31-day month, then if the day fits within that
    if month in [1, 3, 5, 7, 8, 10, 12]:
        if day >= 1 and day <= 31:
            return True
        
        else:
            return False
    
    # checks if month is a 30-day month, and if day fits within that
    if month in [4, 6, 9, 11]:
        if day >= 1 and day <= 30:
            return True
        
        else:
            return False
        
    # checks feb 29 on leap years
    if is_leap_year(year) == True:
        if day >= 1 or day <= 29:
            return True
        
    else:
        return False

def get_month_name(month):
    '''returns a given month as a string'''
    if month == 1:
        return 'January'
    
    if month == 2:
        return 'February'
    
    if month == 3:
        return 'March'
    
    if month == 4:
        return 'April'
    
    if month == 5:
        return 'May'
    
    if month == 6:
       return 'June'
   
    if month == 7:
        return 'July'
    
    if month == 8:
        return 'August'
    
    if month == 9:
        return 'September'
    
    if month == 10:
        return 'October'
    
    if month == 11:
        return 'November'

    if month == 12:
        return 'December'
    
    elif month < 1 or month > 12:
        return 'Invalid Month!'
    
def is_valid_date(month, day, year):
    '''tests given month, day, and year to see if it's T/F, if False, an explanation is given'''
    if is_valid_month(month) == True and is_valid_day_in_month(month, day, year) == True:
        return True
    
    # elif is_leap_year(year) == True:
    #     return 
    # don't need because its already in is_valid_day_in_month fxn
    
    elif is_valid_month(month) == False:
        return f'{month, day, year} is not a valid date, because {month} is not a valid month'
    
    # elif is_valid_day_month(month, day, year) == False:
        # return f'{month, day, year} is not a valid date, because {day} is not a valid day in {month}’
        

if __name__ == '__main__':
    
# is_valid_month test cases
    # print('is_valid_month(10)', is_valid_month(10))
    # print('is_valid_month(138)', is_valid_month(138))
    # print('is_valid_month(-138)', is_valid_month(-138))
    
# is_leap_year test cases
    # print('is_leap_year(138000)', is_leap_year(138000))
    # print('is_leap_year(9100)', is_leap_year(9100))
    # print('is_leap_year(2004)', is_leap_year(2004))
    # print('is_leap_year(2002)', is_leap_year(2002))
    # print('is_leap_year(2023)', is_leap_year(2023))
    
# is_valid_day_month test cases
    # print('is_valid_day_in_month(10, 9, 2002)', is_valid_in_day_month(10, 9, 2002))
    # print('is_valid_day_in_month(10, 32, 2002)', is_valid_in_day_month(10, 32, 2002))
    # print('is_valid_day_in_month(9, 31, 2002)', is_valid_in_day_month(9, 31, 2002))
    # print('is_valid_day_in_month(9, 30, 2002)', is_valid_in_day_month(9, 30, 2002))
    # print('is_valid_day_in_month(9, 31, 2002)', is_valid_in_day_month(9, 31, 2002))
    # print('is_valid_day_in_month(2, 29, 2002)', is_valid_in_day_month(2, 29, 2002))
    # print('is_valid_day_in_month(2, 29, 2000)', is_valid_in_day_month(2, 29, 2000))

# get_month_name test cases
    print('get_month_name(10)', get_month_name(10))
    print('get_month_name(14)', get_month_name(14))
    
# is_valid_date test cases
    print('is_valid_date(10, 9, 2002)', is_valid_date(10, 9, 2002))
    print('is_valid_date(13, 9, 2002)', is_valid_date(13, 9, 2002))
    print('is_valid_date(2, 29, 2002)', is_valid_date(2, 29, 2002))