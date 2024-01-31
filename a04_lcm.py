# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 11:31:56 2023

@author: bayst
"""

# File: a04_lcm.py
# your name: Ding Xin
# your email: dmx@bu.edu
# U63555835
# CS108 A1

from a04_tvm import present_value_of_annuity
from a04_tvm import annuity_payment
from a04_tvm import dollar_format

def calculate_smooth_consumption(age_now, retirement_age, income, assets, rate):
    '''calcs and returns smooth consumption, the average rate at which an individual consumes 
    throughout their lifetime (both working and retirement), with the given parameters'''
    
    # first thing to do is find out amount of working years the user has left and to use 
    # dollar_format on user's income
    
    working_years_remaining = retirement_age - age_now
    
    print(f'You have {working_years_remaining} working years with an annual income of {dollar_format(income)}.')
    # print("income: ", dollar_format(income))
    
    # next we must calc human capital, basically the sum of annuity payments at a discounted 
    # rate, with the present_value_annuity fxn
    
    human_capital = present_value_of_annuity(rate, working_years_remaining, income)
    
    print(f'The present value of your human capital is about {dollar_format(human_capital)}.')
    # print("human capital: ", dollar_format(human_capital))
    
    # next calc economic net worth (human capital + assets)
    
    economic_net_worth = human_capital + assets
    
    print(f'Your financial assets are: {dollar_format(assets)}.')
    # print('assets', assets) # ignore
    # print("financial assets: ", dollar_format(assets))
    
    print(f'Your economic net worth is: {dollar_format(economic_net_worth)}.')
    # print("economic net worth: ", dollar_format(economic_net_worth))
    
    # calc annual consumption, but we need to find years of consumption (100 - age),
    # then multiply with annuity_payment
    
    years_of_consumption = 100 - age_now
    
    annual_consumption = annuity_payment(rate, years_of_consumption, economic_net_worth)
    
    # print("annual consumption: ", dollar_format(annual_consumption))
    
    # then we must find annual savings required (income - consumption)
    
    annual_savings_required = income - annual_consumption
    
    print()
    print(f'Based on your resources, your sustainable annual consumption to age 100 is {dollar_format(annual_consumption)}.')
    print(f'To achieve this consumption , you must save {dollar_format(annual_savings_required)} per year during your working years.')
    # print("save", dollar_format(annual_savings_required), "per year")
    
    # return float(annual_consumption * years_of_consumption)
    return annual_consumption

def interactive_life_cycle_model():
    '''collect inputs from user'''
    
    print("Hello, welcome to the interactive life cycle model.")
    
    age_now = int(input("What is your current age? "))
    
    retirement_age = int(input("At what age do you plan to retire? "))
    
    working_years_remaining = retirement_age - age_now
    
    income = int(input("What is your current annual income? "))
    
    assets = int(input("What is the value of your current financial assets? (if you have none type 0, if in debt, type a negative number) "))
    
    rate = float(input("What is your rate of return on a risk-free, inflation-index investment? "))
    
    human_capital = present_value_of_annuity(rate, working_years_remaining, income)
    
    economic_net_worth = human_capital + assets
    
    years_of_consumption = 100 - age_now
    
    annual_consumption = annuity_payment(rate, years_of_consumption, economic_net_worth)
    
    annual_savings = income - annual_consumption
    
    calculate_smooth_consumption(age_now, retirement_age, income, assets, rate)
    
    print("You have ", working_years_remaining, " working years with an annual income of ", dollar_format(income))
    print("The present value of your human capital is about ", dollar_format(human_capital,))
    print("Your financial assets are: ", dollar_format(assets))
    print("Your economic net worth is: ", dollar_format(economic_net_worth))
    print()
    print("Based on your resources, your sustainable annual consumption to age 100 is ", dollar_format(annual_consumption), " per year.")
    print("To achieve this consumption, you must save", dollar_format(annual_savings), "per year during your working years.")
    
if __name__ == '__main__':
    
    # interactive_life_cycle_model()
    
    # test cases
    
    # calculate_smooth_consumption(23, 67, 45000, 0, 0.02)
    print('calculate_smooth_consumption(23, 65, 50000, 0, 0.03)', calculate_smooth_consumption(23, 65, 50000, 0, 0.03))
    # calculate_smooth_consumption(21, 65, 65000, 0, 0.02)