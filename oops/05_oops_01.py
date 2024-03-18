"""
Object Oriented Programming
"""


class Car(object):
    wheels =4 # member variable
    def __init__(self, make,model='CDZ110i'):
        self.make = make
        self.model=model

    def info (self):
        print("make of the car: "+ self.make)
        print("model of the car: "+ self.model)


c1 = Car('BMW')
print(c1.make)
print(c1.model)
c1.info()

c2 = Car('HONDA','BENZ')
print(c1.make)
print(c1.model)

#print(c2.wheels) # this is not a proper way to call class variable to call class variable use class name
print("wheels=" + str(Car.wheels))


c3 = Car('AUDI','BENZ')
c3.wheels=3
c3.info()
print("wheels="+str(c3.wheels))

print()
print(Car.wheels)




