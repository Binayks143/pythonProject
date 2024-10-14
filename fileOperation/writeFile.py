file =open("bintest.txt",'w')
file.write("hello dear")
file.close()


file=open("bintest.txt")
content=file.read()
print(content)
file.close()

file=open("bintest.txt","a")
file.write("\nbye bye")
file.close()

file=open("bintest.txt",'r')
content=file.read()
print(content)

with open("bintest.txt") as reader:
    content=reader.readlines()
    reverseContent=content[::-1]
    with open("bintest.txt",'w') as writer:
        writer.writelines(reverseContent)
    with open("bintest.txt") as reader:
        final=reader.read()
        print(final)