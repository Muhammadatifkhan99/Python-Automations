import re


# result = re.search(r"aza","plaza")
result = re.search(r"aza","bazaar")
#the r inside the seach function indicates RAWSTRING and tells the 
#interpreter to interpret the python string as it is............
print(result)

result = re.search(r"aza","Maze")
print(result)

result = re.search(r"^x","xenon")
print("Using circumflex: ",result)

result = re.search(r"p.ng","penguin")
print("Using the dot wildcard: ",result)


# to ignore a case sensitivity use the the function re.IGNORECASE

result = re.search(r"p.ng" ,"Pangea", re.IGNORECASE)
print(result)