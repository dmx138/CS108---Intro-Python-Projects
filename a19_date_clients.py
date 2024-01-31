# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 13:48:45 2023

@author: bayst
"""

# File: a19_date_clients.py
# your name: Ding Xin
# your email: dmx@bu.edu
# U63555835
# CS108 A1

from a19_date import Date


def get_age_on(birthday, other):
    '''returns the age of the user depending on the Date's of birthday and other'''
    
    # age = birthday.days_between(other) // 365
    # print(birthday.days_between(other))
    # print(age)    
    
    years = other.year - birthday.year
    # print(years)
    # print(birthday.month)
    # print(other.month)
    # print(birthday.month > other.month)
    
    if birthday.month > other.month:
            
        return years - 1
          
    elif other.month == birthday.month and birthday.day > other.day:
        
        return years - 1

    else:

        return years 
    

def print_birthdays(filename):
    '''reads a .txt file and returns a printout in the format: name (mm/dd/yyyy) (day)'''
    
    file = open(filename, 'r')
    
    # iterate over each line
    for line in file:
        
        # getting rid of the empty lines in between
        line = line.strip()
        
        # using split to get each term without the commmas
        line = line.split(',')
        # print(line)
        
        # set param eters for our Date class
        month = int(line[1])
        # print(month)
        day = int(line[2])
        year = int(line[3])
        
        # set Date to a variable, d and find the day of the week it is on
        d = Date(month, day, year)
        weekday = d.day_of_week()
        # print(d)
        
        # accumulate into the result
        print(f'{line[0]} ({month:02.0f}/{day:02.0f}/{year}) ({weekday})')
        
    file.close()
        
if __name__ == '__main__':
    # birthday = Date(9,26,2012)
    # other = Date(4,17,2023)
    birthday = Date(9,26,2012)
    other = Date(10,2,2023)
    age = get_age_on(birthday, other)
    # print(age)
    # filename = 'birthdays.txt'
    # f = open(filename)
    # text = f.read()
    # f.close()
    print_birthdays('birthdays.txt')