list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
noncommon=[]
common=[]
# non common
for i in list1:
    if i not in list2:
        noncommon.append(i)
for i in list2:
    if i not in list1:
        noncommon.append(i)
print(noncommon)

# common
for i in list1:
    for j in list2:
        if i==j:
            common.append(i)
print(common)