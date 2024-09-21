users = [
    {'eid':1,'ename':'Nixie','email':'nmacquist0@walmart.com','gender':'Female'},
    {'eid':2,'ename':'Joyce','email':'jnoell1@earthlink.net','gender':'Female'},
    # (other users omitted for brevity)
    {'eid':50,'ename':'Dee dee','email':'dcooke1d@nationalgeographic.com','gender':'Female'}
]

print("User Name")

""" for user in users :
    print(user['ename']) """
i = 0
while i < len(users):
    print(users[i]['ename'])
    i += 1  # Increment i inside the loop
