
def is_prime(n):
    if n <= 1:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False
    return True


n = 100

l = []

for i in range(n):
    if is_prime(i):
        l.append(i)
print("prime number is", l)
