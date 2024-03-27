l=[]
lr=int(input("Enter Lower range: "))
ur=int(input("Enter upper range: "))
for i in range(lr,ur):
    if i%2==0:
        l.append(i)
print(l)