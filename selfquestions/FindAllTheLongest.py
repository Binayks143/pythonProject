sentence = "Python is coding"

s1=sentence.split()
longest=""
for i in s1:
    if len(i)>len(longest):
        longest=i
print(longest)

for i in s1:
    if len(i)==len(longest):
        print(i)