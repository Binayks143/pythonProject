#Python Program to Print All Letters Present in Both Strings

string1="Hello"
string2="World"

word=[]
for i in string1:
    if i not in word:
        word.append(i)

for i in string2:
    if i not in word:
        word.append(i)
print(word)


#or
uniquechar=set(string1+string2)
word=list(uniquechar)
print(word)