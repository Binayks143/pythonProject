# wipro

# take two list and sort the element
#To sort the list l and assign the sorted list to l1,
# you should first sort l, and then assign it to l1 in two separate steps:

l1=['C','A','E']
l2=['B','D','F']

l=[]

for i in l1:
    l.append(i)
for i in l2:
    l.append(i)
#accending sorting
l.sort()
print(l)

#decending sorting
l.sort(reverse=True)
print(l)


#another way
l2=sorted(l)
print(l2)

#sorting the string when conations both upper case and lower case
l12=['A','b','C','l','z','F','K','B']

sorted_list=sorted(l12, key=lambda x: x.lower())
print(sorted_list)

