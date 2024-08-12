import re


# # result = re.search(r"aza","plaza")
# result = re.search(r"aza","bazaar")
# #the r inside the seach function indicates RAWSTRING and tells the 
# #interpreter to interpret the python string as it is............
# print(result)

# result = re.search(r"aza","Maze")
# print(result)

# result = re.search(r"^x","xenon")
# print("Using circumflex: ",result)

# result = re.search(r"p.ng","penguin")
# print("Using the dot wildcard: ",result)


# # to ignore a case sensitivity use the the function re.IGNORECASE

# result = re.search(r"p.ng" ,"Pangea", re.IGNORECASE)
# print(result)

# result = re.search(r"[Pp]ython", "Python")
# print(result) 


# result = re.search(r"[a-z]way"," This is the end of the highway")
# print("Specifying the range of the characters followed:",result)

# result = re.search(r"cloud[a-zA-Z0-9]","cloudy")
# print("Specifying the range of the characters:",result)

# result = re.search(r"cloud[a-zA-Z0-9]","cloud9")
# print("Specifying the range of the characters:",result)

# result = re.search(r"cloud[a-zA-Z0-9]","cloudY")
# print("Specifying the range of the characters:",result)

# result = re.search(r"cat|dog","dogs")
# print(result)

# This function only defines the first occurance of the character matching the regax function 


# result = re.search(r"cat|dog","I like both dogs cats")
# print("printing the first occurance of the match:",result)

# To solve this issue we use the findall function 

# result = re.findall(r"cat|dog","I like both dogs cats")
# print("printing the first occurance of the match:",result)


# Repeatition Qualifiers:::

# print(re.search(r"Py.*n", "Pygmalion"))
# print(re.search(r"Py.*n", "Python Programming"))


# print(re.search(r"Py[a-z]*n", "Python Programming"))

# Escape characters::::::::::


# print(re.search(r".com","welcome"))

# print(re.search(r"\.com","www.google.com"))

#backslash matches letters numbers and underscores 

# print(re.search(r"\w*","This is an example"))
# print(re.search(r"\w*","This_is_another_example"))


# backslash \d for matching digits;::
# backslash \s for mathcing whitespace 
# backslash \b for mathcing word boundries


# Names that starts and ends with a with as many characters as possible in the mid.....

print(re.search(r"A.*a", "Austrila"))

# this will print names that begins and ends with the name A..the following sequnce won't match anymore...
print(re.search(r"^A.*a$", "Azerbaijan"))
