import csv

# CSV files are stored in plain text and a single represent a single data record in CSV file
# Each field is separated by comma, with the content of the file stored between the comma
# 
# f = open("simplecsv.csv")
# csv_f = csv.reader(f)
# for row in csv_f:
#     name, phone, role = row
#     print("Name: {}, Phone: {}, Role: {}".format(name, phone, role))
# f.close()

# hosts = [["workstation.local", "192.168.25.46"],["webserver.cloud", "10.2.5.6"]]
# with open('hosts.csv', 'w') as hosts_csv:
#     writer = csv.writer(hosts_csv)
#     writer.writerows(hosts)


#the writerow() is a function that writes one row at a time while writerows write multiple rows at a time

f = open("hosts.csv")
file = csv.reader(f)
for row in file:
    name, address = row
    print("Name: {}, Address: {}".format(name,address))
f.close()