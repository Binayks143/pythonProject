def reverse_string(data):
    non_space_char=[char for char in data if char !=' ']
    reversedSentence=non_space_char[::-1]
    s=[]
    for i in data:
        if i==' ':
            s.append(' ')
        else:
            s.append(reversedSentence.pop(0))
    return ''.join(s)

Input= "The quick brown fox  jumps over the lazy    dog."

s1=reverse_string(Input)
print(s1)
