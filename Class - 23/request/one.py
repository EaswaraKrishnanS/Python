import json
import csv

customer = [
    {'id' : 100, 'name' : 'Aathithya', 'avail' : True},
    {'id' : 101, 'name' : 'Rahul', 'avail' : False},
    {'id' : 102, 'name' : 'Siva Balan', 'avail' : False}
]

fp1 = open('emp.json','w')
fp2 = open('emp.csv','w',newline='')

json.dump(customer,fp1)
print('JSON File Has Been Created Successfully')

wr = csv.writer(fp2)
wr.writerow(['id' , 'name' , 'avail'])
for cust in customer :
    wr.writerow([cust['id'] , cust['name'] , cust['avail']])
print('CSV File Has Been Created Succesfully')

fp1.close()
fp2.close()