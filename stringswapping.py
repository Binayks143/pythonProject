"""Given a sentence containing multiple words, sort the words based on their character length in ascending order.

If two or more words have the same character length, sort those words in alphabetical (ascending) order.
"""

sen= "xyz hi my name is binay working in ravi room abc"
l=sen.split()
print(l)
l1=[]

for i in range(len(l)):
    for j in range(i+1,len(l)):

        if len(l[i])>len(l[j]) or (len(l[i])==len(l[j]) and l[i]>l[j]):
            l[i],l[j]= l[j],l[i]


print(l)
print(' '.join(l))

l.sort(key=lambda x: (len(x), x))
print("other method \n", l)