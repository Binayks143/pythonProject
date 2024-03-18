class Car():
    def __init__(self):
        print("Car instance")

    def drive(self):
        print("car started")

    def stop(self):
        print("car stop")


class BMW(Car):
    def __init__(self):
        super().__init__()
        #Car().super()
        print("BMW class INSTANCE")


c = Car()
c.drive()
c.stop()

b = BMW()
b.drive()
b.stop()
