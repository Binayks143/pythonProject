numbers = [1, 2, 3, 5, 6]
max1=max(numbers)
print(max1)
l1=[]
for i in range(1,max1+1):
    if i not in numbers:
        l1.append(i)
print(*l1)