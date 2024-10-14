#once the file is open and doing read then cursor whill be available at last postion after reading.
file=open("demo.txt")
# specificDate=file.read(6)
# print(specificDate)
alldata=file.read()
print(alldata)
file.close()

# read the file line by line

file=open("demo.txt")
print("reading line")
data=file.readline()
data=file.readline()

print(data)
file.close()

#reading line using loop

file=open("demo.txt")
print("multiple line using loop")
line=file.readline()
while line != "":
    print(line)
    line=file.readline()
file.close()


### readlines
print("readlines ")
file=open("demo.txt")
lines=file.readlines()
print(lines)
file.close()

file=open("demo.txt")
for file in file.readlines():
    print(file)
file.close()

