class Car():
    def __init__(self):
        print("car instance")
    def carStart(self):
        print("Car started")
    def carStop(self):
        print("car Stopped")

class electricCar(Car):
    company="jhj"
    def __init__(self):
        super().__init__()
        print("electric car")
    def carStart(self):
        print("Electric start started")
    def carStop(self):
        super().carStop()
    @classmethod
    def binay(cls,name):
        cls.company=name


c1=Car()
c1.carStart()
c1.carStop()
c2=electricCar()
c2.carStart()
c2.carStop()
# c2.binay()
print(c2.company)
print(electricCar.company)

electricCar.binay("noi")
print(electricCar.company)

