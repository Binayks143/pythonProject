#Python Program to Check if the Substring is Present in the Given String

inputString=input("Enter the string: ")
inputSubString=input("Enter the Sub String:")

if inputSubString in inputString:
    print(f"{inputSubString} is presnet in '{inputString}'")
else:
    print(f"{inputSubString} is not presnet in '{inputString}'")
