# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 00:34:14 2023

@author: bayst
"""

# File: a20_marathon.py
# your name: Ding Xin
# your email: dmx@bu.edu
# U63555835
# CS108 A1

from a19_date import Date

class Marathon(Date):
    # takes on attributes of Date
    
    def __init__(self, new_month, new_day, new_year, name, state):
        '''initializes new attributes on top of the pre-existing Date attributes'''
        super().__init__(new_month, new_day, new_year)
        
        # initialize superclass only attributes
        
        self.name = name
        self.state = state
    
        
    def __repr__(self):
        '''overwrites the __repr__ method from Date for Marathon class objects only'''
        s = f'{self.name}, {self.state} ({self.month:02.0f}/{self.day:02.0f}/{self.year})'
        return s
    
    
    def get_name(self):
        '''returns self.name'''
        return self.name
    
    
    def get_state(self):
        '''returns self.state'''
        return self.state
        
if __name__ == '__main__':
    boston = Marathon(4, 17, 2023, "Boston Marathon", "MA")
    # print(boston)
    print(boston.get_name())
    print(boston.get_state())
    