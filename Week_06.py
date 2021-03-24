# Monday: Dictionaries
empty = {}
print(type(empty))


person = {"name": "Mattia Pivetta"}
print(person)
print(person["name"])

customer = {"name": "Mattia Pivetta", "age": "33"}
print(customer)
print(customer["name"])

# there is a second way that is used to retrive a value from a dictionary
# get(). Hower get() does not give an error if the key does not exists
print(customer.get("name"))
print(customer.get("age"))
print(customer.get("address"))  # no error

# Dictianory with list
data = {"sports": ["Baseball", "Football", "Volleyball"]}
print(data["sports"][0])

sports = ["Basketball", "Baseball", "Football"]
# sposts_dics = {sports}

sposts_dics = {"dic": sports}

print(sposts_dics)

# It is possible to nest dictionaries into list
# and dictionaries into dictionaries

# Monday exercises:
# 1. User input
person = {"name": "", "age": ""}
name = input("What is your name?")
age = input("What is you age?")

person["name"] = name
person["age"] = age

print(person)

# 2. Accessing Ingridients
pizza = {"ingridients": ["cheese", "sausage", "peppers"]}

for i in pizza["ingridients"]:
    print(i)
