n=int(input("Enter a number: "))

def decimalToBinary(n):
    if n==0:
        return ''
    else:
        return decimalToBinary(n//2)+str(n%2)

a=decimalToBinary(n)
print(a)