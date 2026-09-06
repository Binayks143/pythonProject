class Company:
    name="CYZ"

    @classmethod
    def updateCompanyName(cls,name):
        cls.name=name

    @staticmethod
    def add(a,b):
        return a+b
print(Company.name)
Company.updateCompanyName("jooo")
print(Company.name)
print(Company.add(4,3))