a="Python is easy"

a1=a.split(" ")
print(a1)
l=[]
for i in a1:
    l.append(i[::-1])
print(l)

print(*l)
print(" ".join(l))
