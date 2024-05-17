from numpy import *

arr1=array([2,3,4,5,6,6])
arr2=array([7,8,89,4,3,3])

final_array=arr1+arr2
print("vectorised operation=",final_array)

print("log=",log(arr1))
print("max=",max(arr1))
print("sort=",sort(arr1))

#shallow copy
arr3=arr1
print(id(arr1))
print(id(arr3))

#deep copy
arr4=arr1.copy()
print(id(arr4))
print(id(arr1))
