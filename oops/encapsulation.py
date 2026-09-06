class Bank:
    def __init__(self, acc, salary):
        self.acc = acc  # Public
        self._branch = "Bangalore" #Protected/Internal convention but same as public
        self.__salary = salary  #Private-like

o1=Bank(5555555,90000)
print(o1.acc)
print(o1._branch)
# print(o1.__salary) #AttributeError: 'Bank' object has no attribute '__salary'
o1.__salary=70000
print(o1.__salary)
print(o1._Bank__salary)


class Account:
    def __init__(self,name,salary):
        self.name=name
        self.__salary=salary

    def get_salary(self):
        return self.__salary

    def set_salary(self,salary):
        if salary>0:
            self.__salary=salary

a1=Account("binay",800000)
print(a1.name,a1.get_salary())
a1.set_salary(900000)
print(a1.name,a1.get_salary())
print(a1._Account__salary)



