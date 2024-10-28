# list=[6,4,44] # largest and smallest

l = int(input("enter the total number: "))
l1 = []
for i in range(l):
    t1 = int(input("enter the number: "))
    l1.append(t1)

print("original list", l1)


def max_num(l1):
    max_number = float('-inf')
    for i in l1:
        if i > max_number:
            max_number = i
    return max_number


def min_num(l1):
    min_number = float('inf')
    for i in l1:
        if i < min_number:
            min_number = i
    return min_number


max = max_num(l1)
print("max number=", max)

min = min_num(l1)
print("min number=", min)
