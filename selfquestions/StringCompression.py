s="aabcccccaaa"
# a2b1c5a3
count=1
result=""
for i in range(1,len(s)):
    if s[i]==s[i-1]:
        count=count+1
    else:
        result+=s[i-1]+str(count)
        count=1
result +=s[-1]+str(count)
print(result)
