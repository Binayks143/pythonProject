#To check if a given string or number is a palindrome,
def palindromeCheck(input):
    inputValue=str(input)

    if inputValue==inputValue[::-1]:
        return True
    else:
        return False

input_value=input("Enter the string or number: ")

if palindromeCheck(input_value):
    print(input_value,"is palindrome")
else:
    print(input_value,"is not palindrome")

