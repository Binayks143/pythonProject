# input="I am an Indian"
# "IamanIndian"

str = str(input("enter the string any: "))

newstring = str.split()
newstring1 = ''.join(newstring)
print(newstring1)
d = {}
for i in newstring1.lower():
    if i in d:
        d[i] += 1

    else:
        d[i] = 1
print("dict is:", d)
l = []
for i in d:
    if d[i] >= 2:
        l.append(i)

print("repeating char is:", l)
index1=[]
for i in range(len(newstring1)):
    if newstring1[i].lower() in l:
        index1.append(i)
print(index1)