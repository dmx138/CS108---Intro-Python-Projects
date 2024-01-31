# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 00:56:09 2023

@author: bayst
"""

# File: a20_marathon_clients.py
# your name: Ding Xin
# your email: dmx@bu.edu
# U63555835
# CS108 A1

from a20_marathon import Marathon

def print_marathon_list(marathons):
    '''prints out the Date and self.name of each item in the list marathons'''
    
    for m in marathons:
        
        # print(m)
        print(f'{m.month:02.0f}/{m.day:02.0f}/{m.year}: {m.name}')
        

def get_counts_by_state(marathons):
    '''procs a list of marathons and returns a dictionary in the format of: [state, count]'''
    
    # define a dict and set d[m.state] = 0 initially
    d = dict([[m.state, 0] for m in marathons])
    # print(d)

    # iterate over the given list
    for m in marathons:
        # print(d[m])
        
        if m.state in d:
            
            # d[m.state] is the number associated with each marathon state
            d[m.state] += 1
            
            
    return d

def get_days_between_marathons(marathons):
    '''procs the marathons list and returns a list with each Marathon and the number of days since the previous marathon'''
    
    # dbtwn_list = []
    
    marathons.sort()
    
    dbtwn_list = [[marathons[i].days_between(marathons[i - 1]), marathons[i]] for i in range(1, len(marathons))]
    
    return dbtwn_list

    

            

        
    
    
    
if __name__ == '__main__':
    # marathons = [Marathon(1, 8, 2022, "Lake Mead Marathon", "NV"), Marathon(4, 18, 2022, "Boston Marathon", "MA")]
    # print_marathon_list(marathons)
    # marathons = [Marathon(1, 8, 2022, "Lake Mead Marathon", "NV"),
    # Marathon(4, 18, 2022, "Boston Marathon", "MA"),
    # Marathon(4, 30, 2022, "Kentucky Derby Marathon", "KY"),
    # Marathon(5, 1, 2022, "Providence Marathon", "RI"),
    # Marathon(6, 12, 2022, "Maritime Marathon", "WI"),
    # Marathon(7, 30, 2022, "Jack and Jill's Downhill Marathon", "WA"),
    # Marathon(7, 31, 2022, "Jack and Jill's Downhill Marathon", "WA"),
    # Marathon(8, 28, 2022, "Green River Marathon", "VT"),        
    # Marathon(10, 2, 2022, "Maine Marathon", "ME"),
    # Marathon(10, 9, 2022, "Chicago Marathon", "IL"),
    # Marathon(10, 16, 2022, "Bay State Marathon", "MA"),      
    # Marathon(11, 6, 2022, "New York City Marathon", "NY"),
    # Marathon(12, 11, 2022, "Rocket City Marathon", "AL")]
    # print(get_counts_by_state(marathons))
    marathons = [Marathon(1, 8, 2022, "Lake Mead Marathon", "NV"), Marathon(4, 18, 2022, "Boston Marathon", "MA"),
    Marathon(4, 30, 2022, "Kentucky Derby Marathon", "KY")
    ]
    print(get_days_between_marathons(marathons))