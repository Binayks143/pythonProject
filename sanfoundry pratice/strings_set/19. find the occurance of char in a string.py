def char_occurrences(input_string):
    # Initialize an empty dictionary to store character occurrences
    occurrences = {}
    for i in input_string:
        if i in occurrences:
            occurrences[i]+=1
        else:
            occurrences[i]=1
    return occurrences

# Example usage:
input_str = "hello1123"
result = char_occurrences(input_str)
print("Character occurrences:", result)
