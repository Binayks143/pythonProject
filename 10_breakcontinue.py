"""
Break: To break out of the closest enclosing loop
Continue: Go to the start of the closest enclosing loop
else in break loop: else block does not executes if the loop end as a break statement
"""
print("*********** Program 1 *****************")
x = 0
while x < 10:
    print("Value of x is: " + str(x))
    x = x + 1

    if x == 8:
        break
    print("This example is awesome")
    print("*"*20)
print("Just broke out of the loop")

print("*********** Program 2 *****************")

x = 0
while x < 10:
    print("Value of x is: " + str(x))
    x = x + 1

    if x == 5:
        continue
    print("This example is awesome")
    print("*"*20)

print("Just broke out of the loop")


print("*********** Program 3 *****************")

x = 0
while x < 10:
    print("Value of x is: " + str(x))
    x = x + 1

    if x == 8:
        break
    print("This example is awesome")
    print("*"*20)
else:
    print("Just broke out of the loop")