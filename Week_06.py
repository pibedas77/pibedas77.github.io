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

# Tuesday: working with dictionaries

car = {"year": "2018"}
# Adding a key
car["color"] = "Blue"

print("Year: {} \t Color: {}".format(car["year"], car["color"]))

# Changing a value
car["color"] = "Violet"

print("Year: {} \t Color: {}".format(car["year"], car["color"]))

# deleting a key
try:
    del car["year"]
except:
    print("The dictionary key was not fund")

print(car)

# Looping a dictionary
# Looping keys
person = {"name": "Mattia", "age": "33"}
for key in person.keys():
    print(key)

# Looping on values
person = {"name": "Mattia", "age": "33"}
for value in person.values():
    print(value)

# Looping Key-value Pairs
person = {"name": "Mattia", "age": "33"}
for key, value in person.items():
    print("{} and {}".format(key, value))

# User Input
person = {"name": "", "address": "", "number": ""}
person["name"] = input("Hi, what is your name?")
person["address"] = input("What is your address?")
person["number"] = input("What is your number?")

print("These are de details you gave...")
for v in person.values():
    print(v)

# Thursday: Reading and writing files
# Opening/Creating and writing to a txt file
f = open("test.txt", "w+")
f.write("This is a test")
f.close()

# Reading from a txt file
f = open("test.txt", "r")
data = f.read()
f.close()

print(data)

# Writing to csv file
import csv

with open("test.csv", mode="w", newline="") as f:
    writer = csv.writer(f, delimiter=",")
    writer.writerow(["Name", "City"])
    writer.writerow(["Mattia", "Villorba"])

# Reading from csv file

with open("test.csv", mode="r") as f:
    reader = csv.reader(f, delimiter=",")
    for row in reader:
        print(row)


# Thursday exercise
# User input
f = open("testInput.txt", "w+")
ans = input("What is you favourite colour?")
f.write(ans)
f.close()

# Data dumping
import csv

data = {
    "name": ["Dave", "Denis", "Peter", "Jess"],
    "language": ["Python", "C", "Java", "Python"],
}
with open("testDataDumping.csv", mode="w") as f:
    w = csv.writer(f, delimiter=",")
    w.writerow(data.keys())
    w.writerows(zip(*data.values()))

f.close()
