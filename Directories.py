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
# Create a directory and move a file from one directory to another
# using low-level OS functions.

# Check to see if a directory named "test1" exists under the current
# directory. If not, create it:
dest_dir = os.path.join(os.getcwd(), "test1")
if not os.path.exists(dest_dir):
 os.mkdir(dest_dir)

# Construct source and destination paths:
src_file = os.path.join(os.getcwd(), "sample_data", "README.md")
dest_file = os.path.join(os.getcwd(), "test1", "README.md")

# Move the file from its original location to the destination:
os.rename(src_file, dest_file)



# Create a directory and move a file from one directory to another
# using Pathlib.

from pathlib import Path

# Check to see if the "test1" subdirectory exists. If not, create it:
dest_dir = Path("./test1/")
if not dest_dir.exists():
  dest_dir.mkdir()

# Construct source and destination paths:
src_file = Path("./sample_data/README.md")
dest_file = dest_dir / "README.md"

# Move the file from its original location to the destination:
src_file.rename(dest_file)

################################################################################################################
