class number_series():
    def check_number(self,n):
        if n%2==0:
            print ("number is even")
        else:
            print ("number is odd")

n=int(input("Enter a number : "))

ff=number_series()
ff.check_number(n)