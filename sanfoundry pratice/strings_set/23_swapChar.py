def swap_case(s):
    ans = ""
    for i in s:
        if i.isupper():
            ans += i.lower()
        elif i.islower():
            ans += i.upper()

    return ans


s = 'HackerRank.com presents "Pythonist 2".'
result = swap_case(s)
print(result)