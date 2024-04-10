# Python Program to Find Common Characters in Two Strings

string1=input("Enter the first string: ")
string2=input("input second string: ")
common_char=[]
for i in string1:
    if i in string2 and i not in common_char:
        common_char.append(i)
print("Common Char is: ",common_char)


