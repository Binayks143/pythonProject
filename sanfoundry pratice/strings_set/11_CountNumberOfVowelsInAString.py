# Python Program to Count the Number of Vowels in a String

class CountVowels():
    def count_vowel(self,inputstring):
        temp=0
        for i in inputstring:
            if i in('A','E','I','O','U','a','e','i','o','u'):
                temp=temp+1
        return temp


inputstring=input("Enter the String: ")
o1=CountVowels()
result=o1.count_vowel(inputstring)
print(f"Vowels Count in input string {inputstring} is :",result)