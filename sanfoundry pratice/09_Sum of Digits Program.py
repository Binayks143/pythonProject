n=int(input("ENter a number: "))
n1=n
sum=0
while (n>0):
    dig=n%10
    sum=sum+dig
    n=n//10

print(f"sum of digits of number {n1} is : {sum}")
