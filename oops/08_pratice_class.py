class Fruit():
    def __init__(self):
        print("Fruits are rich source of vitamins")

    def nutrition(self):
        print("We will get vitamins A,B C ")

    def fruit_shape(self):
        print("all fruits is having there own shape")


class Mango(Fruit):
    def __init__(self):
        super().__init__()
        print("Mango will come in summer session")

    def nutrition(self):
        print("From mango we will get Vitamins A")

    def color(self):
        print("Mango will be available in yellow and green color")



# F1=Fruit()
# F1.nutrition()
# F1.fruit_shape()


m1=Mango()
m1.nutrition()
m1.fruit_shape()
m1.color()

