a = ['a', 'b', 'a', 'b', 'a', 'a', 'c', 'r', 't', 'rr', 'ad']
d = {}
for i in a:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
print(d)

sorted_key = dict(sorted(d.items(), key=lambda i: i[1], reverse=True))
print(sorted_key)
l = []
for i in d:
    if d[i] >= 2:
        l.append(i)
print(l)



#or

unique = []
duplicate=[]
for i in a:
    if i in unique:
        duplicate.append(i)
    else:
        unique.append(i)

print("duplicate",set(duplicate))
print("unique",unique)