#Two strings are anagrams if they contain the same characters with the same frequency, but the order can be different.

s1="listen"
s2="silent"

if sorted(s1)==sorted(s2):
    print("anangram")
else:
    print("Not Anagram")