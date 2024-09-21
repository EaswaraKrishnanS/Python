import json 

emp_json = """ {
    "eid" : 101,
    "ename" : "Aathithya",
    "avail" : true,
    "loc" : "Pondichery"
} """

emp_dict = json.loads(emp_json)
print(type(emp_dict))
print(emp_dict)