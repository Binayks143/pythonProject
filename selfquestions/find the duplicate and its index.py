# input="I am an Indian"
# "IamanIndian"
input1 = str(input("ENter a string: "))

newstr = input1.split()
newstr1 = ''.join(newstr)
print(newstr1)
d = {}
for i in newstr1:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
print(d)
l = []
for i in d:
    if d[i] >= 2:
        l.append(i)
print(l)
indexlist = []
d1 = {}
for i in range(len(input1)):
    if input1[i] in l:
        if input1[i] in d1:
            d1[input1[i]].append(i)
        else:
            d1[input1[i]] = [i]

print(d1)
