# Monday: Creating and Instatiating a class

# Creating my first class
# class Car:
#     pass


# Creating an Instance
# class Car:
#     pass


# ford = Car()
# subaru = Car()
# print(hash(ford))
# print(hash(subaru))


# Monday exercise
# 1.
class Animal:
    pass


lion = Animal()
tiger = Animal()
print(hash(lion))
print(hash(tiger))

# Tuesday: Attributes


# class Car:
#     sound = "beep"
#     color = "red"


# ford = Car()
# print(ford.color)
# print(ford.sound)

# ford.sound = "honk"
# print(ford.sound)

# Using the __init()__ method


# class Car:
#     def __init__(self, color):
#         self.color = color


# ford = Car("blue")
# print(ford.color)


class Car:
    def __init__(self, color, year):
        self.color = color
        self.year = year


ford = Car("blue", 2018)
subaru = Car("red", 2020)

print(ford.color, ford.year)
print(subaru.color, subaru.year)

# Tuesday exercise
# 1. Dogs


class Dog:
    species = "Canine"

    def __init__(self, name, breed):
        self.name = name
        self.breed = breed


dog1 = Dog("Sammi", "Husky")
dog2 = Dog("Casey", "Chocolate Lab")

print(dog1.name, dog1.breed, dog1.species)
print(dog2.name, dog2.breed, dog2.species)

# 2. User Input


class Person:
    def __init__(self, name):
        self.name = name


ans = input("What is your name?")
person1 = Person(ans)

print(person1.name)
