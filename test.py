a=b=c=0
l=[]
q=[]
p=[]

while a <= 10:
    l.append(a)
    a += 1
print ("value of list is " + str(l))


while b <= 10:
    print("value of list with break is " + str(q))
    q.append(b)
    if b==7:
        break
    b += 1
print("Breaking out from the loop")


while c <= 10:
    p.append(c)
    c += 1
    if c == 5:
        continue
    print("wow"+str(c))
print("breaking out from loop")




