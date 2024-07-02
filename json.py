import json

# Define the list of dictionaries correctly
dict ={ "person":[
    {"name": "mey", "age": 18, "sex": "female"},
    {"name": "bopha", "age": 20, "sex": "female"},
    {"name": "rachana", "age": 19, "sex": "male"}
]}
# Convert the list of dictionaries to a JSON formatted string
data = json.dumps(dict,index=3)
with open("my_data.json","w") as f:
    f.write(data)
    
# for persons in dict:
#     del print(person["name"])
