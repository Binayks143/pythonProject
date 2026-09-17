kl=[23,45,67,22,122,3,3]
largest=float('-inf')
second=float('-inf')
for i in kl:
    if i>largest:
        second=largest
        largest=i
    elif i>second and i != largest:
        second=i



print(largest)
print(second)
