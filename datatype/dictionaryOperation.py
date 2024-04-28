a={1:'Binay',2:'Kiran',4:'harsh'}
print(a)  #print dict

#access value with key
print(a[4])
#print(a[3])     #key error
print(a.get(3))   #don't have data at 3 index
print(a.get(3,'Not available'))   # if data is not available with index then by default we will get given data

#access key
keys=a.keys()
print(keys)
print(list(keys))
value=a.values()
print(value)

#zip function
keys=[1,2,3,4,5]
values=['a','b','c','d','e']
data =dict(zip(keys,values))
print("data=",data)
#added the keys value
data[6]='f'
print("added data=",data)

#delete data
del data[3]
print("deleted data=",data)

#new dict
prog={'js':'atom','cs':'vs','python':["Pychamp","sublime"],'java':{"JEE":"Eclips","JSE":"NetBeans"}}
print("prog=",prog['python'])
print("prog=",prog['python'][1])
print("prog=",prog['cs'])
print("prog=",prog['java']['JEE'])




