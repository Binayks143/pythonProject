#Reverse a String in Python

"""
Reverse a String in Python using Slicing
Reverse a String in Python using Recursion
Reverse a String in Python using Loops
"""
class ReverseAString:
    #Method 1: Reverse a String using Slicing
    def ReverseUsingSlicing(self,input_string):
        return input_string[::-1]

    #Method 2: Reverse a String using Recursion
    def ReverseUsingRecursion(self,input_string):
        if len(input_string)<=1:
            return input_string
        else:
            return self.ReverseUsingRecursion(input_string[1:]) + input_string[0]

    #Reverse a String in Python using Loops
    def ReverseUsingLoop(self,input_string):
        rs=""
        for i in input_string:
            rs=i+rs
        return rs


input_string=input("Enter the string: ")
method1=ReverseAString()

output1=method1.ReverseUsingSlicing(input_string)
output2=method1.ReverseUsingRecursion(input_string)
output3=method1.ReverseUsingLoop(input_string)

print("Reverse of '"+input_string+"' using Slicing is: "+output1)
print("Reverse of '"+input_string+"' using recursion is: "+output2)
print("Reverse of '"+input_string+"' using recursion is: "+output3)


