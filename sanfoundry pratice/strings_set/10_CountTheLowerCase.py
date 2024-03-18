#Python Program to Count Number of Lowercase Characters in a String


def countLowerCase(a):
    temp=0
    for i in a:
        if i.islower()==True:
            temp=temp+1
    return temp

inputstring=input("Enter the string: ")
output=countLowerCase(inputstring)

print(f"Lower case count in a given string '{inputstring}' is {output}")
