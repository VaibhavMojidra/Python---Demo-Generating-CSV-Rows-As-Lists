#Generating CSV - Rows As Lists

import csv

data=[['Ids','Names'],['101','Vaibhav'],['102','Shreyas'],['103','Rohan']]

#Using writerows all data at a time

with open('result1.csv','w') as f1:
    writer=csv.writer(f1)
    writer.writerows(data)

#Using writerow one row at a time 

with open('result2.csv','w') as f2:
    writer=csv.writer(f2)
    for row in data:
        writer.writerow(row)
