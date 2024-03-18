#Python Program to Count the Number of Words and Characters in a String

#counting the char in a word without space
class stringCount:
    temp=0
    def charCount(self,inputstring):
        for i in inputstring:
            if (i==' '):
                continue
            else:
                self.temp=self.temp+1
        return self.temp

    def wordCount(self,inputstring):
        if len(inputstring) == 0:
            return 0
        temp=1
        for i in inputstring:
           if (i==' '):
               temp=temp+1
        return temp


inputstring=input("Enter the string: ")
o1=stringCount()
output1=o1.charCount(inputstring)
output2=o1.wordCount(inputstring)

print(f"Char count of given string '{inputstring}' is {output1}")

print(f"Word count of given string '{inputstring}' is {output2}")
