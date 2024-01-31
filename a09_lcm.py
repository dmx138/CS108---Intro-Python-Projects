# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 11:56:37 2023

@author: bayst
"""

# File: a09_lcm.py
# your name: Ding Xin
# your email: dmx@bu.edu
# U63555835
# CS108 A1

from a04_lcm import calculate_smooth_consumption

def dollar_format(amount):
    '''takes an amount and returns it formatted with commmas and two decimal places'''
    
    # how 
    return f'${amount:,.2f}'

def print_annual_financial_plan(age_now, retirement_age, income, consumption, assets, rate):
    '''uses the calculate_smooth_consumption fxn and uses it to print out a financial with the given parameters
    in a BEAUTIFULLY formatted table'''
    
    # (1) accumulator variables and variables to be used later in printout

    asset_income = 0
    # new_assets = 0
    
    # print(consumption)
    # consumption = calculate_smooth_consumption(age_now, retirement_age, income, assets, rate)

    # heading
    print('Here is an annual summary of your financial plan:')
    print()
    print(f'{"Age":^8}{"Income":13}{"Consumption":16}{"Saving":15}{"Asset Income":15}{"Assets":12}')
    
    # (2) use a loop to collect values
    for i in range(age_now + 1, 101):
        
        savings = income - consumption
        
        # doing - assets prevents assets from going to infinity
        asset_income = assets * rate
        # print(asset_income)
        
        assets += savings + asset_income # problem is here
        # print(assets) 
        
        # (3) accumulate value and print the beeg table
        print(f'{i:^8}{dollar_format(income):13}{dollar_format(consumption):16}{dollar_format(savings):15}{dollar_format(asset_income):15}{dollar_format(assets)}')
        
        if i == retirement_age:
            income = 0
            
        
        # we need to account for assets going below zero
        if assets <= 0:
            print('Out of assets!')
            
            return
        
        

def interactive_life_cycle_model():
    '''collects inputs from user for an interactive version of print_annual_financial_plan fxn'''
    
    print('Welcome to the Personal Financial Calculator.')
    age_now = int(input('Enter your age now: '))
    retirement_age = int(input('Enter your expected retirement age: '))
    # int might be dangerous here
    income = float(input('Enter your current annual income: '))
    assets = float(input('Enter the value of your financial assets: '))
    rate = float(input('Enter the risk-free, real rate of return: '))
    print()
    
    calculate_smooth_consumption(age_now, retirement_age, income, assets, rate)
    
    # define consumption so the fxn doesnt break and die 
    
    consumption = calculate_smooth_consumption(age_now, retirement_age, income, assets, rate)
    
    print_annual_financial_plan(age_now, retirement_age, income, consumption, assets, rate)

    
    
if __name__ == '__main__':
    
    print('print_annual_financial_plan(23, 65, 50000, 40000, 0, 0.03)', print_annual_financial_plan(23, 65, 50000, 40000, 0, 0.03))
    # print('dollar_format(9876543.21)', dollar_format(9876543.21))
    # print('dollar_format(42)', dollar_format(42))
    # print('dollar_format(1234.56)', dollar_format(1234.56))
    # interactive_life_cycle_model()