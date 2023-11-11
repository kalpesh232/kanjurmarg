f = open('MyData.txt','r')
# print(f)
# print(f.read())
# print(f.readline())

# print(f.readline())
# print(f.readline())

# print(f.readline(),end="")
# print(f.readline(),end="")

# print(f.readlines())

# f1 = open('myData1.txt','w')
# f1.write("lapttop\n")

f1 = open('MyData1.txt','a')
# f1.write('hello'+'\n')

# for data in f:
#     f1.write(data)

f3 = open('file.jpeg','rb')
# print(f3.read())

f4 = open('file1.jpeg','wb')
for i in f3:
    f4.write(i)
