# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 10:14:29 2023

@author: bayst
"""

# file: a19_date.py
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
            if self.month == 2 and self.is_leap_year() == True:
                
                self.day = 29
                
                self.month = 2
                
            # if the feb 29 procedures ends up False, go through the month rollover procedure
            else:
            
                self.day = 1
            
                self.month += 1
            
        # account for feb 29 to mar 1
        
        if self.day == 30 and self.month == 2:
            
            self.day = 1
            
            self.month = 3
        
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
    
    def is_before(self, other):
        '''returns True if the date represented by the object comes before the date represented by other
        returns False if on the same day or after other'''
        
        # check year first
        if self.year < other.year:
            
            return True
        
        # if the years are the same, compare months
        elif self.year == other.year and self.month < other.month:
            
            return True
        
        # if the months are the same, compare the days
        elif self.year == other.year and self.month == other.month and self.day < other.day:
            
            return True
        
        # if none of the above conditions are fulfilled, then return False
        else:
            
            return False
            
        
    def is_after(self, other):
        '''returns True if object's date comes after the date represented by other
        returns False if on same day or if object comes before other'''
        
        # just return the opposite output of is_before
        # also return False if the two dates are the same
        if self.is_before(other) == True or self == other:
            
            return False
        
        else:
            
            return True
        # lol
        
        
    def __lt__(self, other):
        '''overrides the < operator in order to compare dates with is_before'''
        
        if self.is_before(other) == True:
        
            return True
        
        else:
            
            return False
        
        
    def __gt__(self, other):
        '''overrides the > operator in order to compare dates with is_after'''
        
        if self.is_after(other) == True:
            
            return True
        
        else:
            
            return False
        
        
    def days_between(self, other):
        '''returns the integer amount of days in between other and self'''
        
        # create deep copies of self and other
        self_copy = self.copy()
        # other_copy = other.copy()
        
        result = 0
        
        # figure out which day comes first and count up using add_one_day until self and other are the same date
        if self_copy.is_before(other) == True:
            
            # print('before')
            
            while self_copy.is_before(other) == True:
                
                # print('before AGAIN')
                # do not set this to a variable as the method returns None
                self_copy.add_one_day()
                    
                result -= 1
                
            return result
        
        elif self_copy.is_after(other) == True:
            
            # print('after')
            
            while self_copy.is_after(other) == True:
                
                self_copy.rem_one_day()
                    
                result += 1
                
            return result
                    
        else:
            
            return result
            
        
    def day_of_week(self):
        '''takes a date and returns the day of the week that the day lies on'''
        
        day_of_week_names = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        
        # begin with a known date of 11/06/23, a Monday
        known_date = Date(11, 6, 2023)
        
        # use days_between function
        days_between = self.days_between(known_date)
        # print(days_between)
        
        modulo = days_between % 7 
        
        return day_of_week_names[modulo]
        
        
        
        
    
        
            
        
            



##########################################################################################                    
if __name__ == '__main__':

    ## TEST CODE HERE:
    # Use these date objects, or create your own. 
    # Uncomment lines below as needed.
    # Test every method thoroughly!

    
    # d1 = Date(12, 1, 2019)
    # d2 = Date(9, 26, 2012)
    d2 = Date(2,12,1809)
    # d1 = Date(12, 10, 2022)
    # d1 = Date(5,3,2023)
    # d1 = Date(11, 16, 2022)
    # d1 = Date(2, 28, 2021)
    # d2 = Date(3, 1, 2021)
    # d1 = Date(2, 28, 2020)
    # d1 = Date(11, 5, 2023)
    # d1 = Date(11, 6, 2023)
    # d2 = Date(3, 1, 2020)
    d1 = Date(4, 17, 2023)
    # d2 = Date(8, 31, 2013)
    # d2 = Date(3, 20, 2020)
    # d2 = Date(11, 18, 2022)
    # d2 = Date(12, 1, 2022)
    # d2 = Date(3, 15, 2020)
    # print(d1.is_before(d2))
    # print(d1.is_after(d2))
    # print(d2.is_after(d1))
    # ny = Date(1, 1, 2023)
    # d = Date(12, 31, 2022)
    # print(d.is_before(ny))
    # print(ny.is_before(d))
    # print(d.is_before(d))
    # print(d1 < d2)
    # print(d1 > d2)
    # print(d2 - 2)
    print(d1.days_between(d2))
    # print(d1.day_of_week())