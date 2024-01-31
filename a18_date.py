# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 10:14:29 2023

@author: bayst
"""

# file: a18_date.py
# starter code by Aaron Stevens (azs@bu.edu)
# ## add your name here!
# Ding Xin (U63555835)
# description: implementation of a Date class to represent a calendar date
# 

##########################################################################################
class Date:
    
    '''creates a Date class that holds attributes of day, month, year'''
    def __init__(self, month, day, year):
        '''Initialize this Date object to set the data attributes 
        to the values passed in as constructor parameters.'''

        self.month = month
        self.day = day
        self.year = year

        # note that this simply sets up the attributes, it doesnt return or print them out
    ##########################################################################################
    def copy(self):
        '''Return a new Date object with the same 
        data attributes as this Date (i.e., a "deep" copy)'''

        d = Date(self.month, self.day, self.year)
        return d
        
   
    ##########################################################################################                    
    ## TO DO: Write your other methods here...
    
    def __repr__(self):
        '''a method that returns the date in an f string formatted as: mm/dd/yy'''
        
        # simply return an f string
        return f'{self.month:02.0f}/{self.day:02.0f}/{self.year:02.0f}'


    def __eq__(self, other):
        '''overrides the == operator to compare the data attributes of two objects'''
        
        return (self.month == other.month and self.day == other.day and self.year == other.year)


    def is_leap_year(self):
        '''when a Date object is created, we will call this method and it will return T/F if self.year a leap year or not'''
        
        # test if year is divisble by 400 or 4
        if self.year % 400 == 0:
            
            return True
        
        if self.year % 100 == 0 and self.year % 400 != 0:
                
            return False 
            
        if self.year % 4 == 0:
           
            return True
        
        else:
            
            return False
        
        
    def is_valid_date(self):
        '''returns T/F if a date is valid or not'''
        
        if self.is_leap_year() == True and self.month == 2 and self.day in range(1, 30):
            
            return True
        
        if self.month not in range(1, 13):
            
            return False
        
        elif self.month in [4, 6, 9, 11] and self.day in range(1, 31):
            
            return True
        
        elif self.month in [1, 3, 5, 7, 8, 10, 12] and self.day in range(1, 32):
            
            return True
        
        else:
            
            return False


    def add_one_day(self):
        '''advances the Date object by one calendar date and updates it'''
        
        # a list of days in the months that we can call on for indexing
        days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
        self.day += 1
            
            
        # when we need to roll over to the next month
        if self.day - 1 == days_in_month[self.month]:
            
            # rolling over a leap year
            if self.month == 2 and self.is_leap_year == True:
                
                self.day = 29
                
                self.month = 2
        
        
        # if the feb 29 procedures ends up False, go through the month rollover procedure
            else:
            
                self.day = 1
            
                self.month += 1
            
        
        # when we need to roll over to the next year
        if self.day == 1 and self.month == 13:
            
            self.month = 1
            
            self.day = 1
            
            self.year += 1
        
    
            

    def rem_one_day(self):
        '''substracts a calendar day from the Date object and updates the Date object accordingly'''
            
        
        # a list of days in the months that we can call on for indexing
        days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
        # this is here for most cases
        self.day -= 1
        
        
        # rolling back to the previous year
        if self.day + 1 == 1 and self.month == 1:
            
            self.month = 12
            
            self.day = 31
            
            self.year -= 1
            
            
        # rolling back to the previous month
        if self.day == 0:
            
            # back to feb 29 on a leap year
            if self.month == 3 and self.is_leap_year() == True:
                
                self.day = 29
                
                self.month = 2
                
            # proceed as normal if leap year condition doesnt apply
            else:
                
                self.month -= 1
                
                self.day = days_in_month[self.month]
                
        
    def add_n_days(self, n):
        '''adds n calendar days to a Date object and adjusts the printout accordingly'''
        
        # print(self)
        
        for i in range(n):
            
            self.add_one_day()
            
            # print(self)
            
            
    def rem_n_days(self, n):
        '''subtracts n calendar days from a Date object and adjusts the printout accordingly'''
        
        # print(self)
        
        for i in range(n):
            
            self.rem_one_day()
            
            # print(self)
            
            
    def __add__(self, n):
        '''__add__ in general overrides the + operator'''
        '''in this case, we want to use this method to override the + opeartor with our add_n_days method'''
        
        # this copy variable has the specific data attributes as our Date objects
        # its not simply a string that reads a date
        copy = self.copy()
        
        # add n calendar days, a copy MUST be returned or else our new variable returns 'None'
        copy.add_n_days(n)
        
        
        # within Python, there exists two 'copies' of our data
        # "self" is the original copy that is inputted clientside
        # "copy" was created within this add method with the use of our copy method, and it is a modified version of "self" essentially
        
        # print(self)
        # print(copy)
        
        
        return copy
        
        
    def __sub__(self, n):
        '''overrides the - operator with our rem_n_days method'''
        
        # call the copy method to create a workable copy of our clientside code
        copy = self.copy()
        
        # subtract n calendars and update our copy variable
        copy.rem_n_days(n)
        
        return copy
                
    
    def __iadd__(self, n):
        '''overrides the += operator with our __add__ and add_n_days methods'''
        
        # the copy method is not called because the += operator naturally updates and reassigns the original Date object
        
        self.add_n_days(n)
        
        return self
    
    def __isub__(self, n):
        '''overrides the -= operator with our __sub__ and rem_n_days methods'''
        
        self.rem_n_days(n)
        
        return self
        
            



##########################################################################################                    
if __name__ == '__main__':

    ## TEST CODE HERE:
    # Use these date objects, or create your own. 
    # Uncomment lines below as needed.
    # Test every method thoroughly!

    # d = Date(8, 26,2001)
    # print('d =', d)
    
    # m = Date(4, 17,2023)
    # print('m =', m)

    # m1 = Date(4, 17, 2023)
    # m2 = Date(4, 17, 2023)
    # print(m1 == m2) 
    # print(m1.year)
    
    # d1 = Date(2, 29, 1900)
    # print(d1.is_leap_year())
    # d2 = Date(2, 29, 2048)
    # print(d2.is_leap_year())
    
    # d1 = Date(4, 18, 2022)
    # print(d1.is_valid_date())
    # # True

    # d2 = Date(14,2,2022)
    # print(d2.is_valid_date())
    # # False

    # d3 = Date(2,30,2022)
    # print(d3.is_valid_date())
    # # False

    # d4 = Date(2,29,2020)
    # print(d4.is_valid_date())
    # # True

    # d5 = Date(2,29,2022)
    # print(d5.is_valid_date())
    # # False

    # d6 = Date(-4,-4, -5)
    # print(d6.is_valid_date())
    # # False

    # d7 = Date(2,29,1900)
    # print(d7.is_valid_date())                                                                                                                                                                                              
    # False
    
    # d = Date(3, 31, 2022)
    # d = Date(3, 1, 2022)
    d = Date(12, 31, 2022)
    # d = Date(1, 1, 2022)
    # d = Date(2, 28, 2020)
    # d = Date(2, 28, 2021)
    # d = Date(3, 1, 2020)
    # d = Date(3, 1, 2021)
    # d = Date(3, 1, 1900)
    # d.add_one_day()
    # d.add_one_day()
    # d.rem_one_day()
    # d.add_n_days(5)
    # d.rem_n_days(5)
    # print(d)
    
    # print(d + 2)
    # print(d - 2)
    # d += 2
    d -= 2
    print(d)