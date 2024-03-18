#Python Program to Calculate the Length of a String Without using Library Functions

class lengthCount:
    def stringCount(self,inputString):
        temp=0
        for i in inputString:
            temp=temp+1
        return temp

inputstring=input("Enter the String: ")
o1=lengthCount()
output=o1.stringCount(inputstring)
print(f"Length of input string '{inputstring}' is : {output}")
print("With Predefiend method :", len(inputstring))

