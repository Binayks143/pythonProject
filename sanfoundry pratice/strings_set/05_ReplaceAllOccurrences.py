# Python Program to Replace All Occurrences of ‘a’ with $ in a String

def replace1(InputString,InputChar,ReplaceWith):
    temp=""
    for i in InputString:
        if i==InputChar:
            temp=temp+ReplaceWith
        else:
            temp=temp+i
    return temp

def replace2(InputString,InputChar,ReplaceWith):
    return InputString.replace(InputChar,ReplaceWith)

InputString=input("Enter a String: ")
InputChar=input("Enter the char which you want to replace: ")
ReplaceWith=input("Enter the char which you want to replace with :")

method1=replace1(InputString, InputChar, ReplaceWith)
print("method1= ",method1)

method2=replace2(InputString, InputChar, ReplaceWith)
print("method2= ",method2)

