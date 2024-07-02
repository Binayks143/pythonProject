dict1={"a":13,"b":145,"e":56,"c":1}

####Sorting by Keys

new_dict=dict(sorted(dict1.items()))
print("sorted by keys:",new_dict)

for key in new_dict:
    print(f"{key}:{dict1[key]}")


###Sorting by values
dict2=dict(sorted(dict1.items(),key=lambda item:item[1]))
print(dict2)
