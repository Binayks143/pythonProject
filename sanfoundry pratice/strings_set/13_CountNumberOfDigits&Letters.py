# Python Program to Count the Number of Digits and Letters in a String


def CountDigitLetters(inputString):
    digit_count=0
    char_count = 0
    for i in inputString:
        if i.isdigit():
            digit_count=digit_count+1
        #if i.isalpha():
        if ((i >= 'a' and i <= 'z') or (i >= 'A' and i <= 'Z')):
            char_count += 1
    return  digit_count, char_count

inputString=input("Enter the String : ")

d_count, c_count =CountDigitLetters(inputString)
print(f"Nos of digit in entered string '{inputString}'  is {d_count} and letters is {c_count}")