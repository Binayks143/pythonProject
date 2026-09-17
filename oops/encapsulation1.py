# "Encapsulation means wrapping data and the methods that operate on that data inside a class
# and controlling direct access to the data. In Python, I can use __ to make an attribute
# private and provide methods such as getter and setter methods to access or modify it

class bankAcc:
    def __init__(self,account_holder,balance):
        self.account_holder=account_holder
        self.__balance=balance

    def deposit(self,amount):
        self.__balance+=amount

    def withdrow(self,amount):
        if amount<self.__balance:
            self.__balance-=amount
        else:
            print("insufficient balance")

    def get_balance(self):
        return self.account_holder, self.__balance

o1=bankAcc("Binay",9000000)
o1.deposit((80000))
o1.withdrow(100000)
print(o1.get_balance())
print(o1._bankAcc__balance)
# ("Double underscore triggers name mangling. It makes the attribute difficult to access directly and helps prevent accidental access or overriding. However, "
 # "it can still technically be accessed using the mangled name.")

