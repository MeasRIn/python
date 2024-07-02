# cafe_menu = {
#     "Espresso": 2.50,
#     "Latte": 3.00,
#     "Cappuccino": 3.20,
#     "Mocha": 3.50,
#     "Americano": 2.75
# }
# obj1={'name':'oyery','age':18}

# obj2={'age':19,'name':'oyery'}
# obj1 == obj2

# user=input(" Chooes Cafe :")
# if user.lower() == "espresso":
#     cafe = cafe_menu["Espresso"]
#     print(f" Price = {cafe}") 

# delete=input("Enter Name:")
# if delete.lower == "espresso":
#     del cafe_menu["Espresso"]
# print(cafe_menu)

# import json
# data='{"title":"test","ISBM":12344}'
# json_data=json.load(data)
# print(type(json_data))
# print(json_data["title"])
# print(json_data["ISMB"])

# import json
# data='{"title":"test","ISBM":12344}'
# json_data=json.load(data)
# with open('book.json','w') as f:
#     json.dump(json_data,f,indent='\t')
import json

# Define the list of dictionaries correctly
people = [
    {"name": "mey", "age": 18, "sex": "female"},
    {"name": "bopha", "age": 20, "sex": "female"},
    {"name": "rachana", "age": 19, "sex": "male"}
]

# Convert the list of dictionaries to a JSON formatted string
data = json.dumps(people)

for person in people:
    print(person["name"])

