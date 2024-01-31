# -*- coding: utf-8 -*-
"""
Created on Wed Sep  6 22:07:31 2023

# file: a01_change.py
# author: Ding Xin 
# email: dmx@bu.edu
# BUID: U63555835

# To make the autograder script work, you will need to follow these constraints:
# * You must have variables named price, change, quarters, dimes, nickels,
#   and pennies. You may include any additional variables you choose.
# * In your finished code, put all print statements at the bottom 
#   (as indicated by the comment).
#   You may use print statements elsewhere in your code while you are developing
#   and testing, but you should comment out those print statements before submission. 



# once you have a working solution, you should change this line to test other 
# starting values, e.g., 68 cents, 69 cents, etc. to ensure that your calculations 
# work for each value.
price = 67

# do all of your computations here:
"""
price =   59    

# must first find change

change = 100 - price

# subtract as many quarters from change. find how many quarters used (w/ " // ") and remaining cents w/ modulo (" % ")

quarters = 25

Qused = change // quarters

Qchange = change % quarters

# take remaining cents after quarters used (Qchange), use " // " to find how many dimes used, then find remaining cents w/ modulo ("%")

dimes = 10

Dused = Qchange // dimes 

Dchange = Qchange % dimes

# repeat w/ nickels

nickels = 5

Nused = Dchange // nickels

Nchange = Dchange % nickels

# finally, repeat w/ pennies

pennies = 1

Pused = Nchange // pennies

Pchange = Nchange % pennies

# put all print statements in this section:
print('The price is', price,'cents.')  

print('change is', change, 'cents')

print('quarters:', Qused)

print('dimes:', Dused)

print('nickels:', Nused)

print('pennies:', Pused)