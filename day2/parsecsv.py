'''
load the emps.csv file into the memory then read all the data from the file and
remove email column  and remaining data write it in another csv file in csv format
Use Logging here. 
'''
import csv

with open("emps.csv","r") as fr:
    csv_data=csv.DictReader(fr)
    with open("newemps.csv","w") as fw:
        columns=['fname','lname']
        csvwriter=csv.DictWriter(fw,fieldnames=columns,delimiter=',',lineterminator='\n')
        csvwriter.writeheader()
        for row in csv_data:
            del row['email']
            csvwriter.writerow(row)

print("Process done")



