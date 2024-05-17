'''
*kwargs: if we are calling without eky and value

if we are calling the function with key and value
**kwargs is short for "keyword arguments".
It's a dictionary that stores keyword arguments passed to a function.
The name "kwargs" is arbitrary; you can use any name as long as you prefix it with two asterisks (**).
The syntax **kwargs allows you to pass a variable number of keyword arguments to a function.

'''

def person(name,*data):

    name=name
    print(name)

    print(data)

person("hari",90,"BLR",9090909002)

#if we are calling person funcation with key and  value itwill through error
# person(name="hari",age=90,add="BLR",PhNo=9090909002)

def person1(name,**data):
    name=name
    print(name)
    print(data)
    for i,j in data.items():
        print(i,j)

person1(name="hari",age=90,add="BLR",PhNo=9090909002)
