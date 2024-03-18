"""
Variable Scope
"""

a = 10   # global variable


def atest_method(a):
    print("Value of local 'a' is: " + str(a))
    a = 2
    print("New value of local 'a' is: " + str(a))


print("Value of global 'a' is: " + str(a))
atest_method(a)
print("Did the value of global 'a' change? " + str(a))


print("************ changing the global variable ***************")

a = 10


def atest_method():
    global a   # using the global variable inside the method
    print("Value of 'a' inside the method is: " + str(a))
    a = 2  # changing the gloabl variable
    print("New value of 'a' inside the method is changed to: " + str(a))


print("Value of global a is: " + str(a))
atest_method()
print("Did the value of global 'a' change? " + str(a))
