
def remove_duplicate(inputString):
    countdict={}
    fianlList=[]
    #taking the dictionary with count
    for i in inputString:
        if i in countdict:
            countdict[i]+=1
        else:
            countdict[i]=1

    #filter the dictionary whose key's value =1
    for i in countdict:
        if countdict[i]==1:
            fianlList.append(i)
    return fianlList

a="testbinay1231"
print(remove_duplicate(a))
print("output=",''.join(remove_duplicate(a)))