num=int(input("Enter a number : "))
temp=num
rev=0
while (num>0):
    a=num%10
    rev=rev*10+a
    num=num//10

print("Reverse number is : ",rev)

# Other way
reverse= int(str(temp)[::-1])
print ("Reverse number another way : ",reverse)