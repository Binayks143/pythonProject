l=[4,5,63,3,7,6]
target=9
pairs=[]

for i in range(len(l)):
    for j in range(i+1,len(l)):
        if l[i]+l[j]==target:
            pairs.append((l[i],l[j]))
print(pairs)
for i in pairs:
    if sum(i)==target:
        print(True)
    else:
        print(False)