import os

# print("The current working directory is: " + os.getcwd())

# os.makedirs("new dir")

# os.chdir("new dir")
# print(os.getcwd())

# os.mkdir("atif1")
# os.mkdir("atif2")
# os.mkdir("atif3")
# os.rmdir("atif")
# os.rmdir("new dir")

dir = "basicscripts"
for name in os.listdir(dir):
     fullname = os.path.join(dir, name)
     if os.path.isdir(fullname):
          print("{} is a directory".format(fullname))
     else:
          print("{} is a file".format(fullname))