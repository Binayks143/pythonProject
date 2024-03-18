#Python Program to Determine How Many Times a Given Letter Occurs in a String Recursively

class OccuranceChar:
    def OccuranceCount(self,inputstring,inputchar):
        if len(inputstring)==0:
            return 0
        else:
            if inputstring[0]==inputchar:
                return 1+ self.OccuranceCount(inputstring[1:],inputchar)
            else:
                return self.OccuranceCount(inputstring[1:],inputchar)

inputstring=input("Enter the String : ")
inputchar=input(f"Enter the char to count in '{inputstring}' :")
o1=OccuranceChar()
count=o1.OccuranceCount(inputstring.lower(),inputchar.lower())
print(f"The character '{inputchar}' occurs in '{inputstring}' is : {count}")




