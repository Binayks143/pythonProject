from PIL.ImageOps import autocontrast

input="automation"

def test1(a):
    for i in a:
        if a.count(i)==1:
            return i
    return None

print("first non repeating char",test1(input) )


