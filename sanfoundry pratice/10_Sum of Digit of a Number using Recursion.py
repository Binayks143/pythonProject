def fun1(n):
    if n<10:
        return n
    else:
        dig=n%10
        return dig+fun1(n//10)

n=int(input("Enter the number: "))
a=fun1(n)
print(a)