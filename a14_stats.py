# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 01:37:33 2023

@author: bayst
"""

# File: a14_stats.py
# your name: Ding Xin
# your email: dmx@bu.edu
# U63555835
# CS108 A1

def mean(values):
    '''calcs the mean of a set of values'''
    
    # accumulator variable for the sum
    summation = 0
    
    # def loop to acccumulate variables
    for i in list(values):  
        # print(i)
        
        # accumulate
        summation += i
        
    number_of_values = len(values)
    # print(number_of_values) # prints 8 
    
    mean = summation / number_of_values
    
    return mean



def variance(values):
    '''calcs and returns variance of a set of values'''
    
    summation = 0
    
    for i in list(values):
        # print(i)
        squared_deviations = (i - mean(values)) ** 2
        # print(inner_value)
        
        # accumulate squared deviations
        summation += squared_deviations
        
    number_of_values = len(values)
    
    return summation / number_of_values



def stdev(values):
    '''calcs and returns SD of a set of values'''
    
    return variance(values) ** 0.5


def max_of_list(values):
    '''processes a list and returns the maximum value'''
    
    # set the max as the first value as a baseline
    maximum = values[0]
    # print(maximum)
    
    # iterate every value in the list
    for i in list(values):
        
        # replace the maximum if i is greater
        if i > maximum:
            
            maximum = i
            
            
    return maximum


def min_of_list(values):
    '''procs a list and returns the minimum value'''
    
    minimum = values[0]
    
    for i in list(values):
        
        if i < minimum:
            
            minimum = i
            
    return minimum


def describe(values):
    '''procs a list of values and returns a set of descriptive statistics for the list'''
    
    result = 'Descriptive Statistics: \n'
    
    
    count = len(values)
    
    result += f'count: {count}\n'
    
    
    minimum = min_of_list(values)
    
    result += f'min: {minimum:.2f}\n'
    
    
    maximum = max_of_list(values)
    
    result += f'max: {maximum:.2f}\n'
    
    
    average = mean(values)
    
    result += f'mean: {average:.2f}\n'
    
    
    variance_ = variance(values)
    
    result += f'variance: {variance_:.2f}\n'
    
    
    standard_deviation = stdev(values)
    
    result += f'stdev: {standard_deviation:.2f}\n'
    
    
    return result
    
    
def covariance(x, y):
    '''calculates covariance  of a set of values'''
    
    # accumulator variable to sum up products of x and y differences
    summation = 0
        
    # use an index-based loop to iterate over positions
    for i in range(len(x)):
        

        
        # x differences from the mean
        
        mean_x = mean(x)
        
        x_differences = x[i] - mean_x
        # print(x[i])
        
        
        # y differences from the mean
        
        mean_y = mean(y)
        
        y_differences = y[i] - mean_y
        # print(y[i])
        
        
        # products of x and y differences
        
        products_of_xy_differences = x_differences * y_differences
        
        # sum up products of x and y differences with accumulator
        
        summation += products_of_xy_differences
        
        # define N
        
    number_of_values = len(list(x))
        
        
    return summation / number_of_values
   

def correlation(x, y):
    '''calcs correlation of a set of values'''
    
    # set variable for covariance
    
    covariance_xy = covariance(x, y)
    
    
    # set variable for stdev of x and y
    
    sd_x = stdev(x)
    
    sd_y = stdev(y)
    
    
    # wham bam thank you mam correlation
    
    return covariance_xy / (sd_x * sd_y)
    
    
def rsq(x, y):
    '''calcs and returns the square of correlation between two sets x and y'''
    
    return correlation(x, y) ** 2


def simple_regression(x, y):
    '''calcs and returns the intercept, and alpha and beta regression coefficients'''
    
    # beta coefficient
    
    beta = covariance(x, y) / variance(x)
    
    
    # alpha coefficient
    
    alpha = mean(y) - (beta * mean(x))
    
    
    # le printout
    
    return alpha, beta
        
        
        
    




if __name__ == '__main__': 
    # values = [4, 7, 9, 2, 8, 5, 1, 6]
    values =  [46, 82, 72, 21, 38, 39, 24, 48, 5, 36]
    # values = [4,4,3,6,7]
    # values = [6,7,5,10,12]
    x = [4,4,3,6,7]
    y = [6,7,5,10,12]
    # print(mean(values))
    # print(variance(values))
    # print(stdev(values))
    # print(max_of_list(values))
    # print(min_of_list(values))
    print(describe(values))
    # print(covariance(x, y))
    # print(correlation(x,y))
    # print(rsq(x, y))
    # print(simple_regression(x, y))
    # print('my_sum(values)', my_sum(values))