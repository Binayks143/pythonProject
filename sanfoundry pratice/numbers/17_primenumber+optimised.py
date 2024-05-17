def is_prime(number):
    if number <=1:
        return False
    elif number == 2:
        return True
    else:

        for i in range(3, int(number **0.5) +1,2 ):
            if number %i==0:
                return False
        return True



number=13
if is_prime(number):
    print(number, "is prime")
else:
    print(number, "is not prime")