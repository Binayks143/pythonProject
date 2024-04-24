#I am Binay
#I ma yaniB



def reverse_word(string):
    word=string.split()
    l=[]
    for i in word:
        reverse_word=i[::-1]
        l.append(reverse_word)

    reverse_string=' '.join(l)
    return reverse_string



input = "I am Binay"

o1=reverse_word(input)
print("reverse word in a string is:" ,o1)





