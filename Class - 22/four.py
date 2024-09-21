import json

fp1 = open('data.json','r')

users = json.load(fp1)

print(type(users))

male_users = list(filter(lambda user : user['gender'] == 'Male',users))

fp2 = open('male.json','w')

print(len(male_users))
print('Male File Created')

json.dump(male_users,fp2)

female_users = list(filter(lambda user : user['gender'] == 'Female',users))

fp3 = open('female.json','w')

print(len(female_users))
print('Female File Created')

json.dump(female_users,fp3)

fp1.close()
fp2.close()
fp3.close()