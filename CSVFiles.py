import csv

# CSV files are stored in plain text and a single represent a single data record in CSV file
# Each field is separated by comma, with the content of the file stored between the comma
# 
f = open("simplecsv.csv")
csv_f = csv.reader(f)
for row in csv_f:
    name, phone, role = row
    print("Name: {}, Phone: {}, Role: {}".format(name, phone, role))
f.close()