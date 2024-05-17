a=10            #Global Variable

def globaltest():
    global a   #here marking a as global variable
    a=9         #Local Variable, by doing this it will change the global variable
    print("Inside function: ",a)

globaltest()

print("outside fun: ",a)


#Note with same variable we can not use global and local to achive this we can use globals()

b=21
c=21
d=33
print(id(b))
def globaltest2():
    b=11
    # x=globals()    # x will conatins all the value of b,c,d
    x=globals()['b']
    print(x)
    print("inside function: ",b)
    globals()['b']=990   #changing the global value


globaltest2()
print("Outside function: ",b)



