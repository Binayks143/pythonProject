#create a array using user input and search the element

import array as arr

#empty array
a1=arr.array('i',[])

inp1=int(input("Enter the number of int elemet in a array: "))

for i in range(inp1):
    a2=int(input("Enter the element to add in array: "))
    a1.append(a2)
print("Final array is :", a1)

#To search the elment in a array:
s1=int(input("Enter the element to search in the array"))

k=0
#option1
for i in a1:
    if i == s1:
        print("element found at index", k)
        break
    k+=1
else:
    print("element not found")

#option 2
element=a1.index(s1)
print(element)

