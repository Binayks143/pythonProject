#bluevine 1st round


# Given an array containing None values, fill in the None values with the most recent non None value in the array.
# For example, for array1= [1, None, 2, 3, None, None, 5, None]
# Output should be: [1, 1, 2, 3, 3, 3, 5, 5]

def listoperation(l):
    if not l:  # Handle the case where the list is empty
        print("List is empty")
        return l

    l1 = len(l)
    t = 0
    previous = None

    # Handle the initial None values if the list starts with None
    if l[0] is None:
        for i in range(l1):
            if l[i] is not None:
                previous = l[i]
                break
        if previous is not None:  # Fill the initial None values with the first non-None value found
            for i in range(l1):
                if l[i] is not None:
                    break
                l[i] = previous

    # Replace None values with the previous non-None value
    for i in range(len(l)):
        if l[i] is None:
            t += 1
            l[i] = previous
        else:
            previous = l[i]

    if l1 == t:
        print("All elements are None")

    return l

# Test cases
l1 = [None, None, None, None]
print("output =", listoperation(l1))

l2 = [None, 1, None, 2, None]
print("output =", listoperation(l2))

l3 = [1, None, 2, None, 3]
print("output =", listoperation(l3))

l4 = []
print("output =", listoperation(l4))
