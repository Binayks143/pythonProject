lr=int(input("Enter the lower range limit: "))
ur=int(input("Enter the upper range limit: "))
n=int(input("Enter the number: "))
l=[]
for i in range(lr,ur):
    if (i%n==0):
        l.append(i)

print("numbser are divisible by {} from {} to {} are {}".format(n,lr,ur,l))
# or
print(f"number are divisible by {n} from {lr} to {ur} are {l}")

