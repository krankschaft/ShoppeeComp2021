import json
import pandas as pd
import numpy as np
import csv
import time

#Shopee Competition 2021 - Multi Channel Contacts

start_time = time.time()

df = pd.read_json("C:\\Users\\krank\\Downloads\\contacts.json")

print(df.keys())
print(df)

Att = []
Contacts = []

i = 0
k = 1

#Appending Contacts Libraries for Comparison

for lab, row in df.iterrows() :
    if row['Email'] != "" or row['Phone'] != "" or row["OrderId"] != "" or row["Contacts"] != "" :
        Att.append([i,row['Email'], row['Phone'], row["OrderId"], row["Contacts"]])
    Contacts.append([i, ""])
    i = i + 1
    if int(i / 100000) == k:
            print(str(20*k) + "% Data Appended")
            k=k+1

print("Done Appending Libraries")

i = 0
k = 0

# Collating Contact Entries and Summing of Contacts
Att0 = Att

for w, x, y, z, z1 in Att:
    #print(w, " - ", x, " - ", y, " - ", z, " - ", z1)
    j = 0
    m = 0   #Contact Sum Counter
    for w0, x0, y0, z0, z2 in Att0:
        if (w == w0 and w0 != "") or \
           (x == x0 and x0 != "") or \
           (y == y0 and y0 != "") or \
           (z == z0 and z0 != "") :
            m = m + z2
            Contacts[i][1] = Contacts[i][1] + "-" + str(w0)
        j = j + 1
        if j == 500000:
            break
    Contacts[i][1] = str(Contacts[i][1])[1:] + ", " + str(m)
    i = i + 1
    if int(i / 100000) == k:
            print(str(20*k) + "% Data Collated")
            k=k+1
    #Contacts[0][1] = "1"
    if i == 500: #Limited to 500 rows due to CPU performance: 100rows / 0.4mins
        break

#Output to CSV File
with open("C:\\Users\\krank\\Documents\\PythonOutput\\ShopeeChallenge1.csv", "+w") as my_csv:
    csvWriter = csv.writer(my_csv, delimiter = ';')
    csvWriter.writerows(Contacts)

with open("C:\\Users\\krank\\Documents\\PythonOutput\\ShopeeChallenge1 - Att.csv", "+w") as my_csv:
    csvWriter1 = csv.writer(my_csv, delimiter=';')
    csvWriter1.writerows(Att)

print("CSV File Created.")

print("Total time taken: %s seconds" % (time.time() - start_time))