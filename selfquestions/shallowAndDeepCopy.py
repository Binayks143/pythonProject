import copy

# Original list of lists
original_list = [[1, 2, 3], [4, 5, 6]]

# Create a shallow copy
shallow_copied_list = copy.copy(original_list)
shallow_copied_list[0][0]=100
print(shallow_copied_list)
print(original_list)

# //Deep copy
deep_copy=copy.deepcopy(original_list)
deep_copy[0][0]=500
print(original_list)
print(deep_copy)
