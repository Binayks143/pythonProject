"""
Examples to show how strings works in python

Sequence of characters
Contains a-z, 0-9, @
In double or single quotes
"""

a = "This is a simple string"
b = 'Using single quotes'

print(a)
print(b)

c = "Need to use 'quotes' inside a string"
print(c)

d = "Another way to handle \"quotes\""
print(d)

## \ will ignore the given symbol


## in multi line we can use \
a = "This is a single\
 string"
print(a)

"""
Examples to show available string methods in python
"""

# Accessing characters in a string
# index starts from zero
first = "nyc"[0]
city = "sfo"
print(first)
ft = city[0]
print(ft)


"""
len()
lower()
upper()
str()
"""

stri = "This Is a Mixed Case"
print(stri.lower())
print(stri.upper())
print(len(stri))

print(stri + str(2))

"""
Concatenation
"""
print("Hello " + " " + " World !!!")
print(first + " " + city)


"""
Examples to show available string methods in python
"""

# Replace Method
a = "1abc2abc3abc4abc"
print(a.replace('abc', 'ABC'))
print(a.replace('abc', 'ABC',2))
#COUNT 2 REPLACE THE NOS OF INTENANCES

# Sub-Strings
# starting index is inclusive
# Ending index is exclusive
su = a[1]
sub = a[1:6]
step = a[1:6:2]

print("****************")

print(su)
print(sub)
print(step)

"""
MORE STRING SLICING AND INDEXING
"""

a= "Hi how are you"
print (a[:])
print (a[1:])
print (a[3:])
print (a[:7])
print (a[3:10:2])

print (a[-1])
print (a[:-1])

print (a[-1:])
print (a[-10:])
print (a[-10:-2])
print (a[:len(a)])
print (a[:len(a)-1])
print (a[:len(a)-1])
## reverse a string
print (a[::-1])



"""
Examples to show how string formatting works in python
"""

city = "nyc"
event = "show"

print("Welcome to " + city + " and enjoy the " + event)
print("Welcome to %s" % city)
print("Welcome to %s and enjoy the %s" % (city, event))