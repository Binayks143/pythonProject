import array as arr

v1=arr.array('i',[2,3,4,5])
print(v1)
#print one element
print(v1[2])

v2=arr.array('u',["i","j","k","l"])
print(v2)

#copy the elemet fron array to another
# if we don't know the type then use typecode
v3=arr.array(v1.typecode, (a for a in v1))
print(v3)

v4=arr.array(v1.typecode, (a*a for a in v1))
print(v4)