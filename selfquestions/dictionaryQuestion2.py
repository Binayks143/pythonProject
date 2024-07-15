##aktana
"""
Create and list and from list to dict
and sort the element based on value
and delete one key and value then compair with the initial dict
"""
# list to dictionary:
name = ['A', 'B', 'D', 'C']
memory = [34, 560, 780, 89]

n = dict(zip(name, memory))
print("Dictionary from list is ", n)
n1 = n.copy()

sorted_by_keys = dict(sorted(n.items()))
print("sorted_by_keys=", sorted_by_keys)
sorted_by_values = dict(sorted(n.items(), key=lambda item: item[1]))
print("sorted_by_values ", sorted_by_values)
print("Deleting one key and value")
del n1['B']
n1['A']=290
print("after deleting new dict is ", n1)

# comparing the two dictionary
keys1 = set(n.keys())
keys2 = set(n1.keys())
print(keys1)
print(keys2)

common_keys = keys1.intersection(keys2)
different_keys = keys1.symmetric_difference(keys2)

print("common_keys: ", common_keys)
print("different_keys: ", different_keys)

# compair the different values

for i in common_keys:
    if n[i]==n1[i]:
        print(f"Value for key '{i}' is same and value is : {n[i]}")
    else:
        print(f"value for key '{i}' is different and value is : {n[i]} in dict n and {n1[i]} in dict n1")



