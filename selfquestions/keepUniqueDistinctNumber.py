# list is given and delete any two element so that you will be getting least unique element.

l = [1, 1, 1, 2, 2, 3, 4, 5, ]

d = {}
for i in l:
    if i in d:
        d[i] += 1

    else:
        d[i] = 1

sorted_value = dict(sorted(d.items(), key=lambda x: x[1]))
len_dict = len(sorted_value)
count = 0
m = 2
for i in sorted_value:

    if count < m:
        l.remove(i);
        count += 1

# print(d)
print(sorted_value)
print(set(l))
