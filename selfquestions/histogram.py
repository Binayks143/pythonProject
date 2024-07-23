"""
    l=[1,2,3,4,5,66,67,88,33,22,34,32,34,45,65,34,39,0]
    output:
    0-10:4
    11-20:6
    21:30:9
.....
"""
def custom_histogram(data):
    #These lines find the minimum and maximum values in the data list
    min_value=min(data)
    max_value=max(data)
    bin_size=10

    #Determining the Histogram Range

    start_range=(min_value//bin_size)*bin_size
    end_range=((max_value//bin_size)+1)*bin_size

    #Creating Bins and Initializing Counts

    bin={}
    for i in range(start_range,end_range,bin_size):
        bin[(i,i+bin_size-1)]=0

    #The keys are tuples representing the range of each bin
    #The values are initially set to 0, representing the count of numbers in each bin.

    #Counting the Numbers in Each Bin
    for i in data:
        for j in bin:
            if j[0] <=i <=j[1]:
                bin[j]+=1
                break
    """
    This nested loop goes through each number in the data list and checks which bin it falls into.
     When a number is found to be within a bin's range, the count for that bin is incremented by 1.
      The break statement ensures we stop checking other bins once we find the correct bin for the 
      current number.
    """
    print(bin)
    for i in bin:
        print(f"{i[0]} - {i[1]} : {bin[i]}")


l=[1,2,3,4,5,66,67,88,33,22,34,32,34,45,65,34,39,0]
print(custom_histogram(l))

