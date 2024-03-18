"""
A group of code statements which can perform some specific task
Methods are reusable and can be called when needed in the code
methods should be in small case
"""
##type """ and enter it to enter default methods template

def abc(a,b):
  """
  get sum of two numbers
  :param a: 
  :param b: 
  :return: 
  """
  print(a+b)

abc(2,7)
abc(9,-5)

print('*'*50)

def sum_nums(n1,n2):
    return n1+n2


sum_nums(5,5) #no output

sum1=sum_nums(6,6)
print(sum1)


def is_metro(n):
    city=["Mumbai","Delhi","Bangalore","Chennai"]
    if n in city:
        return (n +" is metro city")
    else:
        return (n+ " is non metro city")

c1=is_metro("Mumbai")
c2=is_metro("rkl")
print(c1)
print(c2)


"""
Positional Parameters
They are like optional parameters
And can be assigned a default value, if no value is provided from outside
non-default parameter follows default parameter e.g def check(n2,n1=15):
"""
print("********** Positional Parameters ********")

#def check(n1=15,n2): wrong non-default parameter follows default parameter


def check(n2, n1=15):
    return n1+n2


a1 = check(8, n1=3)
print(a1)
a2 = check(6, 9)
print(a2)
a3 = check(n1=77, n2=23)
print(a3)
