import numpy as np
#multiple way to creation a array:
#1. using array()
a1=np.array([22,32,42,2])
print("using array()",a1)

#2. linespace()
#all the value in float
a2=np.linspace(2,10)
print("linespace()",a2)

#3. arrage()
a3=np.arange(10,100,2)
print("using arrage():",a3)

#4 logspace

a4=np.logspace(10,100,5)
print(a4)

#zeros , ones

a5=np.zeros(9)
print(a5)

a6=np.ones(7,int)
print(a6)