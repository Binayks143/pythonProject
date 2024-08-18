import copy

# Original list of lists
original_list = [[1, 2, 3], [4, 5, 6]]

# Create a shallow copy
shallow_copied_list = copy.copy(original_list)

print("Original list:", original_list)
print("Shallow copied list:", shallow_copied_list)
print("ID of original list:", id(original_list))
print("ID of shallow copied list:", id(shallow_copied_list))

# Modify a nested list in the original list
original_list[0][0] = 'X'

print("Modified original list:", original_list)
print("Shallow copied list after modification:", shallow_copied_list)
print("ID of original list:", id(original_list))
print("ID of shallow copied list:", id(shallow_copied_list))



#deep copy:

# Original list of lists
original_list_deep = [[1, 2, 6], [4, 5, 7]]

# Create a deep copy
deep_copied_list = copy.deepcopy(original_list_deep)

print("Original list:", original_list_deep)
print("Deep copied list:", deep_copied_list)
print("ID of original list:", id(original_list_deep))
print("ID of deep copied list:", id(deep_copied_list))

# Modify a nested list in the original list
original_list[0][0] = 'X'

print("Modified original list:", original_list_deep)
print("Deep copied list after modification:", deep_copied_list)
print("ID of original list:", id(original_list_deep))
print("ID of deep copied list:", id(deep_copied_list))

