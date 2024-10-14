def reverseWithSPace(data):
    words = data.split()  # Split the input into words
    reversed_words = [word[::-1] for word in words]  # Reverse each word
    s = list(data)  # Convert the original string into a list of characters to preserve spaces

    word_index = 0
    for i, char in enumerate(s):
        if char != " ":
            # Replace each non-space character with the reversed word's character
            s[i] = reversed_words[word_index][0]
            reversed_words[word_index] = reversed_words[word_index][1:]
            if not reversed_words[word_index]:  # Move to the next word once finished
                word_index += 1

    print("".join(s))

l = "The quick brown fox  jumps over the lazy    dog."
reverseWithSPace(l)
