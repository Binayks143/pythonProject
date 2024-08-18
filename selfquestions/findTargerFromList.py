import asyncio.constants

l=[1,3,5,11]
target=8
s=set()
for i in l:
    for j in l:
        if i+j==target:
            s.add(i)
            s.add(j)

if sum(s)==target:
    print(True)
else:
    print(False)
print(s)
