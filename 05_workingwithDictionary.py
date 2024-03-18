"""
Data type to store more than one value in one variable name, in terms of key value pairs
Dictionary items are in brackets {} in key:value pairs, separated with "," {'k1':'v1', 'k2':'v2'}
Not sequenced, no indexing -> Mapping
"""

car = {'make': 'bmw', 'model': '550i', 'year': 2016}
print(car)

model = car['model']

print(car['make'])
print(model)

d = {}
d['one'] = 1
d['two'] = 2

print(d)

sum_1 = d['two'] + 8
print(sum_1)
print(d)
d['two'] = d['two'] + 8
print(d)

"""
Nested Dictionary:
d = {'k1': {'nestk1':'nestvalue1', 'nestk2': 'nestvalue2'}}
d['k1']['nestk1']
"""

cars = {'bmw': {'model': '550i', 'year': 2016}, 'benz': {'model': 'E350', 'year': 2015}}
bmw_year = cars['bmw']['year']
print(bmw_year)
print(cars['benz']['model'])


"""
Dictionary Methods
"""

car = {'make': 'bmw', 'model': '550i', 'year': 2016}
cars = {'bmw': {'model': '550i', 'year': 2016}, 'benz': {'model': 'E350', 'year': 2015}}

print("key=",car.keys())
print(cars.keys())
print(car.values())
print(cars.values())
print(car.items())

car_copy = car.copy()
print(car_copy)

print(car.pop('model'))
print(car)