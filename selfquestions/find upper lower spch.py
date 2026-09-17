# Count uppercase, lowercase, digits and special characters
sentence ="PyThon@123 hi hello9898"

# s1=sentence.split()
upper=[]
lower=[]
digit=[]
spch=[]
for j in sentence:
    if j.isupper():
        upper.append(j)
    elif j.islower():
        lower.append(j)
    elif j.isdigit():
        digit.append(j)
    else:
        spch.append(j)


print(upper)
print(lower)
print(digit)
print(spch)
