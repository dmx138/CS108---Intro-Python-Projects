# File: a02_stats.py
# your name: Ding Xin
# your email: dmx@bu.edu
# U63555835
# CS108 A1

# TO DO: write your functions here!

def calc_sum(a, b, c, d, e):
    return a + b + c + d + e
    # TO DO:  implement this function and return a value!
    # do not print!
    
def calc_mean(a, b, c, d, e):
    """calcs and returns statistical mean of paramaters"""
    return (calc_sum(a, b, c, d, e)) / 5

def calc_variance(a, b, c, d, e):
    """calcs and returns variance (avg of squared differences from mean) of parameters"""
    m = calc_mean(a, b, c, d, e)
    return (((a - m) ** 2) + ((b - m) ** 2) + ((c - m) ** 2) + ((d - m) ** 2) + ((e - m) ** 2))/5

def calc_stdev(a, b, c, d, e):
    """calcs and returns stdev (sqrt of variance) of parameters"""
    return (calc_variance(a, b, c, d, e)) ** 0.5

# This section contains test cases, which will execute your functions
# and print out the results. These tests are "protected" (by indentation) within 
# an if statement, which will prevent them from running on the Gradescope server.
# You must write all of your test cases within this indented block.
if __name__ == '__main__':

	# make sure all of your test cases are indented by 1 tab, following the example below.
	# declare several variables with which to test the functions
    a = 8
    b = 9
    c = 10
    d = 9
    e = 8

	# We make a function call to the `calc_sum` function,
	# and assign the result into a variable called `sum_of_obs`
    sum_of_obs = calc_sum(a, b, c, d, e) 
    mean_of_obs = calc_mean(a, b, c, d, e) 
    variance_of_obs = calc_variance(a, b, c, d, e)
    stdev_of_obs = calc_stdev(a, b, c, d, e)
    
	# now we print out this variable
    print("The sum of observations is:", sum_of_obs)
    print("The mean of observations is:", mean_of_obs)
    print("The variance of observations is:", variance_of_obs)
    print("The stdev of observations is:", stdev_of_obs)
	# TO DO: you need to call each of your other functions below, 
	# and verify the results by printing them out
	
	




## DO NOT WRITE ANY TEST CASES IN THE GLOBAL SCOPE (i.e., at the left margin of the file).