import json

fp1 = open('users.json','r')

users = json.load(fp1)

print(type(users))

employee = []

for user in users :
    employee.append({
        "eid" : user['id'],
        "ename" : user['name'],
        "email" : user['email']
    })

fp2 = open('emp.json','w')

json.dump(employee,fp2)

print('New File Has Been Created')

fp1.close()
fp2.close()