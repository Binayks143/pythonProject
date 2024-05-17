import numpy as np

a=np.array([
    [2,2,3],
    [2,4,6]])
print(a)
print("dimension=",np.shape(a))

print("dattype=",np.ndim(a))
print("dimension= (2d or 3d)",np.ndim(a))
print("size=",np.size(a))

#From 2d array to 1 d array
singleDim=a.flatten()
print(singleDim)

#from 1 d to 3d array
a2=np.array([3,4,6,7,8,1,2,3,3,22,33,0])
threeDarray=a2.reshape(2,2,3)
print("1d to 3 d \n",threeDarray)

