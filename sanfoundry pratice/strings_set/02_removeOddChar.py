#Python Program to Remove Odd Indexed Characters in a string

def removeOddChar(givenString):
    temp=""
    for i in range(len(givenString)):
        if i%2==0:
            temp=temp+givenString[i]
    return temp


givenString=input("Enter the String : ")

t1=removeOddChar(givenString)
print(t1)

