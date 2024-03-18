"""
Excecute statements repeatedly
conditions are used to stop the execution of loop
Iterable items are List,tuple,strings,dictionary
"""

##string
mystring="Hello Baby"
for a in mystring:
    if a== "l":
        print("L", end='')
    else:
        print(a,end='')


##List
car=["BMW", "HONDA", "SUZUKI", "MARUTI", "TATA"]
for i in car:
    print(i)

#tuple for loop
n=(10,18,9,2,7,3)
for i in n:
    print(i*5)

#Dictionary for loop
d={"a":"apple","b":"Boy","c":"cat"}

for keys in d:
    print("Keys = :",keys, end=" ")
    print("and values is ",d[keys], end=" ")
    print("\n")

#keys and values both
for k,v in d.items():
    print(k," ", v)


#Zip funtion: Itterating multiple lists at same time
# Take the sortest list and make the pair.
l1=[2,5,88,9,10]
l2=[1,11,22,33,44,55,66,77]

for a,b in zip(l1,l2):
    if a>b:
        print(a)
    else:
        print(b)


# range function:

"""
Built-in function
Creates a sequence of numbers but does not save them in memory
Very useful for generating numbers
"""

a3 = range(0, 20, 6)
print(a3)
print(type(a3))

print(list(a3))


l = [1, 2, 3]

for num in range(1, 4):
    print(num)


