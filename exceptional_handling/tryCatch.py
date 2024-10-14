# with open("notavailable.txt",'r') as reader:
#     content=reader.read()
#     print(content)

# In above code we will be getting FileNotFoundError exception.

try:
    with open("binay12.txt", 'r') as reader:
        content = reader.read()
        print(content)
except:
    print("File not available")

# In above code if file not available then getting except block is executing
# if file available then except block is not excetuing

# suppose if we want to get the actual exception from python then use following code

try:
    with open("demo1.txt",'r') as reader:
        print(reader.read())

except Exception as e:
    print("File not available",e)


finally:
    print("closing the file")

