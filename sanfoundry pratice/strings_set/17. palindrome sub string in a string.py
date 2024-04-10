#Find the palindrome sub string in a string

def ispalindrome(a):
    return a==a[::-1]

def checkispalindrome(s):
    l=[]
    n=len(s)
    for i in range(n):
        for j in range(i+1,n+1):
            substring=s[i:j]
            if ispalindrome(substring) and len(substring)>1:
                l.append(substring)

    return l
inputstring="abghmomhjj"

o1=checkispalindrome(inputstring)
print("palindrome substring in {} are: {}".format(inputstring,o1))


