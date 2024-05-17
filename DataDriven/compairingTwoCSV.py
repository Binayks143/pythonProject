import csv
import pathlib
#Best one
#configuring the path
path = "C:\\Users\\SC-229-USER\\Desktop\\sweta\\"
file_name1 = "hp_random"
file_name2 = "lp_random"

file_loc1 =  path + str(file_name1)+str(".csv")
file_loc2 =  path + str(file_name2)+str(".csv")


# Read the first CSV file

with open(file_loc1,'r') as file1:
    reader1=csv.reader(file1)
    row1=list(reader1)


# Read the Second CSV file
with open(file_loc2,'r') as file2:
    reader2=csv.reader(file2)
    row2=list(reader2)
# Find the difference rows between the two files
diff_row=[]

for i in row1:
    if i not in row2:
        diff_row.append(i)

for i in row2:
    if i not in row2:
        diff_row.append(i)

# Write the difference rows to a new CSV file
with open('diff.csv','w',newline='') as diff_file:
    writer=csv.writer(diff_file)
    writer.writerows(diff_row)
