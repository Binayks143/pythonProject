"""
Some built-in functions
max(): It takes any number of arguments and returns the largest one.

min(): It takes any number of arguments and returns the smallest one.

abs(): It returns the absolute value of the number, that number's distance from 0.
It always returns a positive value and it only takes a single number.

type(): It returns the type of the data it receives as an argument.

*args : will take multiple arguments
"""


def largest_num(*args):
    return max(args)


def smallest_num(*args):
    return min(args)


l = largest_num(11, 234, -844, 0, 678, 9898, 3)
s = smallest_num(11,234,-844,0,678,9898,3)
print("largest num is :"+ str(l))
print("smallest num is :"+str(s))


def absolute_value(a):
    return abs(a)


print("absolute_value is", absolute_value(10))
print("absolute_value is", absolute_value(-10))
