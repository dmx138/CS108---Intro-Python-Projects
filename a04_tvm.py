# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 10:30:58 2023

@author: bayst
"""

# File: a04_tvm.py
# your name: Ding Xin
# your email: dmx@bu.edu
# U63555835
# CS108 A1

def future_value(r, n, pv):
    '''calcs and returns future value (FV) of lump sum (pv) invested 
    at rate (r) for n periods'''
    # formula for future value
    return pv * ((1 + r) ** n)

def present_value(r, n, fv):
    '''calcs and returns the present value (pv) of lump sum (fv), 
    DISCOUNTED at rate (r) for n periods'''
    # the formula for present value
    return (fv)/((1 + r) ** n)

def present_value_of_annuity(r, n, pmt):
    '''calcs and returns pv of total annuity generated over n periods at rate (r)'''
    # formula for total annuity payment
    pv = ((pmt * (1-((1+r)**(-n)))) / r)
    return pv

def annuity_payment(r, n , pv):
    '''calcs and returns pv of annuity of pmt received each period for n periods,
    discounted at rate (r)'''
    # formula for individual annuity payments
    pmt = (r * pv)/(1 - ((1 + r) ** (-n))) 
    return pmt

def dollar_format(amount):
    '''converts amount of money to whole dollars (no cents) and returns the value as a string'''
    # int is used first to get rid of any decimals, str then takes the int output and turns it into a string
    return '$' + str(int(amount))

# main program:
if __name__ == '__main__':
    
    # test cases:
    
    # future_value
    # print('future_value(0.05, 2, 100)', future_value(0.05, 2, 100))
    # print('future_value(0.08/12, 20*12, 400)', future_value(0.08/12, 20*12, 400))
    
    # # present_value
    # print('present_value(0.06, 5, 1000)', present_value(0.06, 5, 1000))
    # print('present_value(0.06/2, 5*2, 500)', present_value(0.06/2, 5*2, 500))
    
    # # pv of annuity
    # print('present_value_of_annuity(0.05, 30, 250)', present_value_of_annuity(0.05, 30, 250))
    # print('present_value_of_annuity(0.009/12,60, 471.75)', present_value_of_annuity(0.009/12,60, 471.75))
    print('present_value_of_annuity(0.03, 42, 250)', present_value_of_annuity(0.05, 30, 250))
    
    # # annuity payment
    # print('annuity_payment(0.05, 10, 1000)', annuity_payment(0.05, 10, 1000))
    # print('annuity_payment(0.009/12, 60, 27667.44)', annuity_payment(0.009/12, 60, 27667.44))
    
    # # $ format
    # print('dollar_format(123.456)', dollar_format(123.456))
    # print('dollar_format(123456.789)', dollar_format(123456.789))
    