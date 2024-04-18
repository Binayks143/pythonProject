a={1:'Binay',2:'Kiran',4:'harsh'}
print(a)
print(a[4])
#print(a[3])     #error
print(a.get(3))   #don't have data at 3 index
print(a.get(3,'Not available'))   # if data is not available with index then by default we will get given data

#zip function
keys=[1,2,3,4,5]
values=['a','b','c','d','e']
data =dict(zip(keys,values))
print("data=",data)
#added the keys value
data[6]='f'
print("data=",data)

#delete data
del data[3]
print("data=",data)

#new dict
prog={'js':'atom','cs':'vs','python':["Pychamp","sublime"],'java':{"JEE":"Eclips","JSE":"NetBeans"}}
print("prog=",prog['python'])
print("prog=",prog['python'][1])
print("prog=",prog['cs'])
print("prog=",prog['java']['JEE'])
