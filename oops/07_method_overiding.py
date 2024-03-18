class Car(object):
    def __init__(self):
        print("you just created the car instance")

    def drive(self):
        print("Car Started")

    def stop(self):
        print("Car Stopped")


class Bmw(Car):
    def __init__(self):
        print("BMW is luxery car")

    def drive(self):  ## overwriting the parent class method
        print("BMW started")

#calling the parent class 
    # def drive(self):
    #     super(Bmw,self).drive()

c1=Car()
c1.drive()
c1.stop()

b1=Bmw()
b1.drive()


