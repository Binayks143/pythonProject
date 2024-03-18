# Python Program to Count Number of Uppercase and Lowercase Letters in a String

def countUpperCase(inputString):
    count=0
    for i in inputString:
        if i.isupper()==True:
            count=count+1
    return count


def countLowerCase(inputString):
    count=0
    for i in inputString:
        if i.islower()==True:
            count=count+1
    return count



inputString=input("Enter the String: ")
countUC=countUpperCase(inputString)
countLC=countLowerCase(inputString)
print(f"Upper case {countUC} and LowerCase is {countLC}")