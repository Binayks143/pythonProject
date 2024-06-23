l=[2,3,4,5,5]

l1=[i*i for i in l]
print(l1)

l2=[i*i for i in l if i%2==0]
print(l2)

nl=['Odd'+str(i) if i%2!=0 else 'EVEN'+str(i) for i in range(10)]
print(nl)