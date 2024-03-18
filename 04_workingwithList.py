"""
Data type to store more than one value in one variable name
List items are in brackets, separated with "," [ 1, 2, 3 ]
"""

cars = [ "bmw", "honda", "audi"]
empty_list = []
print(empty_list)
print(cars)

print("*#"*20)

print(cars[1])

num_list = [1, 2, 3]
sum_num = num_list[0] + num_list[1]

print(sum_num)

more_cars = [ "bmw", "honda", "audi"]
print(more_cars[1])

more_cars[1] = "Benz"

print(more_cars[1])
print(more_cars)




"""
Built-in methods to help manipulating a list
"""

cars = [ "bmw", "honda", "audi"]

length = len(cars)
print(length)

cars.append("Benz")
print(cars)

cars.insert(1, "Jeep")
print(cars)

x = cars.index("honda")
print(x)

y = cars.pop()
print(y)
print(cars)

cars.remove("Jeep")
print(cars)

print("*#"*20)

slicing = cars[0:2]
a = cars[1:]
print(slicing)
print("a="+ str(a))

print("*#"*20)
print(cars)
cars.sort()

print(cars)