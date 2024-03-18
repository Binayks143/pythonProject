lr=int(input("Enter the lower range limit: "))
ur=int(input("Enter the upper range limit: "))

for i in range(lr,ur):
    if (i%7==0 and i%5==0):
        print(i," are Divisible by 7 and Multiple of 5 in a Given Range")
    # else:
    #     print(i,"Numbers are not Divisible by 7 and Multiple of 5 in a Given Range")