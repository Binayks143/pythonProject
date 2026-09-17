# Create and access a nested dictionary

employee = {
    "emp1": {
        "name": "Binay",
        "age": 25,
        "city": "Bengaluru"
    },
    "emp2": {
        "name": "Rahul",
        "age": 28,
        "city": "Delhi"
    }
}

print(employee["emp1"])
print(employee["emp2"])
print(employee["emp1"]["name"])
print(employee["emp1"]["age"])

for i,j in employee.items():
    print(f"name is {j["name"]} and age is {j["age"]}")