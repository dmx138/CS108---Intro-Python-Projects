# File: a02_functions.py
# your name: Ding Xin
# your email: dmx@bu.edu
# U63555835
#CS108 A1

# function 0: an example of funciton definition
def opposite(x):
    """ returns the opposite of its input
        input x: any number (int or float)
    """
    return -1*x


# put your definitions for the remaining functions below
def cube(x):
    """returns the cubed (^3) input)"""
    return x ** 3

def slope(x1, y1, x2, y2):
    """returns the slope using parameters given"""
    return((y2 - y1) / (x2 - x1))

def cylinder_volume(diameter, height):
    """returns volume of cylinder"""
    return 3.14159 * ((diameter / 2) ** 2) * height

# This section contains test cases, which will execute your functions
# and print out the results. These tests are "protected" (by indentation) within 
# an if statement, which will prevent them from running on the Gradescope server.
# You must write all of your test cases within this indented block.
if __name__ == '__main__':

	# make sure all of your test cases are indented by 1 tab, following the example below.

    # write your test code for all functions below.
    # for example:
    print('opposite(3) =', opposite(3))
    print('cube(6) =', cube(6))
    print('slope(2, 5, 12, 18)', slope(2, 5, 12, 18))
    print('cylinder_volume(10, 10)', cylinder_volume(10, 10))