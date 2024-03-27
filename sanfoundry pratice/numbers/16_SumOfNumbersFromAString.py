# belongs to string objects. It checks whether all the characters in a string are digits.
# It returns True if all characters in the string are digits, and False otherwise.

given_string='Abc544vhnVjn8n0q'
l1=[]
for i in given_string:
    if i.isdigit():
        l1.append(int(i))
print("Sum is: ",sum(l1))

#list containing all string
given_string1=['1','4','T','I','7','0','P','2','T']
l2=[]
for i in given_string1:
    if i.isdigit():
        l2.append(int(i))

print("Sum is: ",sum(l2))


#list containing numbers and strings
given_string2=['1',4,'T','I',7,0,'P',2,'T','8']
l3=[]
# Separate numbers and strings
numbers_set=[x for x in given_string2 if isinstance(x,int)]
strings_set=[x for x in given_string2 if isinstance(x,str)]

print("numbers set is",numbers_set)
print("string set is ",strings_set)
l4=[]
for i in strings_set:
    if i.isdigit():
        l4.append(int(i))

print("Sum is: ",sum(l4)+sum(numbers_set))



