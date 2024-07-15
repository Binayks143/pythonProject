# arrays =[[1,2,3],[4,5,6],[7,8,9]] In this case the median is 5
#
# arrays =[[1,2,3],[4,5],[100,101,102]] In this case the median is 4.5

#####Aktana

def flatten_list(n):
    f=[]
    for i in n:
       f.extend(i)
    print("Combined list= ",f)
    return f


def calculate_median(data):
    if not data:
        raise ValueError("The list is empty")

    data.sort()
    n=len(data)
    mid=n//2

    #even list
    if n% 2==0:
        median=(data[mid-1] +data[mid])/2
    # checking odd place
    else:
        median=data[mid]

    return median


list1=[[1,2,3],[4,5,6],[7,8,9]]

list2=arrays =[[1,2,3],[4,5],[100,101,102]]
data=flatten_list(list2)
median=calculate_median(data)
print(f"the median is: {median}")














