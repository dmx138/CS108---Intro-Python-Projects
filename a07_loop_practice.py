# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 01:28:37 2023

@author: bayst
"""

# File: a07_loop_practice.py
# your name: Ding Xin
# your email: dmx@bu.edu
# U63555835
# CS108 A1

def is_divisor(d,x):
    '''returns true if d is a divisor/factor of x'''
    # modulus (%) detects remainders
    if x % d == 0:
        return True
    
    else:
        return False
    
def is_prime(x):
    '''returns true if integer x is a prime number'''
    # test if #'s that aren't 1 or x are divisors of x, if failed, return false
    for i in range(2 , x):
        if is_divisor(i, x) == True:
            return False
        
    return True

def print_primes(n):
    '''prints out all prime numbers starting from 1, up to n with the help of the is_prime fxn'''
    for x in range(1, n + 1):
        # n + 1: must print out n itself
        
        if is_prime(x) == True:
            print(x, end=', ')
            # 2nd parameter keeps all prints on one line
            
from a04_tvm import future_value

def print_future_values(rate, pv, start_year, end_year):
    '''prints future values of pv given a certain interest rate per year'''
    print(f'Future value of {pv} invested at {rate} per year:')
    print('Year    Future Value')
    # formatting hahahahahahahahahahhahajhahahanhahnahha
    
    for v in range(start_year, end_year + 1):
        # end_year + 1 will include the last year
        fv = future_value(rate, v, pv)
        # v replaces n in the fv fxn
        
        print(f'{v}   $ {fv:05.2f}')
        

if __name__ == '__main__':

    # print('is_divisor(2, 10)', is_divisor(2, 10))
    # print('is_divisor(2, 21)', is_divisor(2, 21))
    # print('is_divisor(5, 385)', is_divisor(5, 385))
    # print('is_prime(2)', is_prime(2))
    print('is_prime(3)', is_prime(3))
    print('is_prime(9)', is_prime(9))
    print('is_prime(11)', is_prime(11))
    # print('is_prime(12)', is_prime(12))
    # print('is_prime(29)', is_prime(29))
    print('is_prime(385)', is_prime(385))
    # print('print_primes(10)', print_primes(10))
    # print('print_future_values(0.06, 100, 10, 15)', print_future_values(0.06, 100, 10, 15))