#Python Program to Remove the nth Index Character from a Non-Empty String

def string_operation1(inputString,nthChar):
    finalString = ""
    for i in range(len(inputString)):
        if(i != nthChar):
            finalString += inputString[i]

    return finalString;

def string_operation2(inputString,nthChar):
    first_part=inputString[:nthChar]
    second_part=inputString[nthChar+1:]
    return first_part+second_part

a=input("Enter a String: ")
b=int(input("Enter the nth char to remove in char : "))
method1=string_operation1(a,b)
method2=string_operation2(a,b)

print("method1=" +method1)
print("method2="+method2)