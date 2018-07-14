import json

data=[]
with open('data.json') as f:
    data = json.load(f)

print("-"*50)

print('{:5} {:10} {:15} {:10}'.format("ID", "FIRST NAME", "LAST NAME", "CITY"))
for item in data:
    print('{:5} {:10} {:15} {:10}'.format(item["id"], item["first_name"], item["last_name"], item["city"]))

print("-"*50)