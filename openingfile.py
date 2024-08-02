
file = open("spider.txt")
# print(file.readline())
# print(file.readline())
print(file.read())
file.close()
#we need to close files because our operating system can create a limited number of file descriptors
#to avoid the race condition we need to close files open 

with open("spider.txt") as file:
    print(file.readline())

#the with automatically close the file and protect to expilicity close files 