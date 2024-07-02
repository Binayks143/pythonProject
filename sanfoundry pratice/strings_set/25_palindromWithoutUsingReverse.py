text='radar'
l=len(text)
fg = 0
for i in range(l//2):
    if text[i] != text[l-1-i]:
        fg = 1
        break
if(fg):
    print("number is not palidrome")
else:
    print("number is palidrome")

