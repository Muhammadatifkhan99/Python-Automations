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

dir = "website"
for name in os.listdir(dir):
     fullname = os.path.join(dir, name)
     if os.path.isdir(fullname):
          print("{} is a directory".format(fullname))
     else:
          print("{} is a file".format(fullname))

# print(os.listdir("website"))
# print(os.path.isdir("atif2"))


################################################################################################################
################################################################################################################
################################################################################################################
# Managing files and directories includes creating, deleting, and moving files and directories. It also includes 
# changing ownership and permissions of
# the files and directories. There are several ways to manage files and directories in Python. One of the easiest
#  ways is to use low-level functions in
# the OS and SYS modules that closely mimic standard Linux commands such as os.mkdir()and  os.rmdir().
#  Alternatively, you can utilize the Pathlib 
# module, which provides an object-oriented interface to working with the file systems. 
################################################################################################################
################################################################################################################
################################################################################################################
