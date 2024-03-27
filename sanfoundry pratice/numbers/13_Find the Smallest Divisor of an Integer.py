n=int(input("Enter a number: "))
l=[]
for i in range (2,1+n):
    if (n%i==0):
        l.append(i)

print("All divisor is",l)
print("The smallest Divisor is :" ,min(l))
