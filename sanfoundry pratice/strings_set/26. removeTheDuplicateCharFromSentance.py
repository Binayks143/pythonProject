##The result is a sentence where duplicate characters are removed from each word.


a = "hello hi  how   are u hello"
a1 = a.split()
l = []
for i in a1:
    """
    set(word) removes duplicates but does not preserve order.
    sorted(set(word), key=word.index)) ensures the original order of characters is maintained.
    """

    uniqueWord = ''.join(sorted(set(i), key=i.index))
    l.append(uniqueWord)

print(' '.join(l))
