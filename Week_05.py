## Functions
# Creating and calling functions

# Monday: creating and calling functions
def printInfo():
    print("Name: Mattia")
    print("Age: 33")


printInfo()
printInfo()


def calc():
    x, y = 10, 15
    print(x + y)


calc()


# Parameters
def printName(name):
    print("Hello {}".format(name))


printName("Mattia")
printName("Camille")
printName(2)

# Multiple parameters
def addCalc(add1, add2):
    result = add1 + add2
    print("The SUM is: {}".format(result))


ans1 = int(input("Type your first number..."))
ans2 = int(input("Type your second number..."))

addCalc(ans1, ans2)

# Passing a list
listnumbers1 = [1, 3, 10, 20]
listnumbers2 = [10, 20, 30, 40]


def squares(nums):
    for num in nums:
        print(num ** 2)


squares(listnumbers1)
squares(listnumbers2)

# Default parameters
# Default parameters MUST ALWAYS GO AFTER non-default parameters
def calcArea(r, pi=3.14):
    area = pi * (r ** 2)
    print("Area: {}".format(area))


calcArea(10)

# Making parameters optional
# we do this by assign an empty string
def printNmaes(first, last, middle=""):
    if middle:
        print("{}, {}, {}".format(first, middle, last))
    else:
        print("{}, {}".format(first, last))


printNmaes("Mattia", "Pivetta", "Marie")
printNmaes("Mattia", "Pivetta")

# *args
# using args parameters to take in a tuple of arbitrary values
def outputData(name, *args):
    print(type(args))
    for arg in args:
        print(arg)


outputData("Jhon Smith", 2, True, "Jess")

# **kwargs
def outputData2(**kwargs):
    print(type(kwargs))
    print(kwargs["name"])
    print(kwargs["num"])


outputData2(name="Jhon Smith", num=33, b=True)

# Tuesday exercise
# 1. User input
def determingFirstLetter(word):
    if word[0].isupper():
        print(True)
    else:
        print(False)


word = input("write a word using upper or lower case...")
determingFirstLetter(word)

# 2. No name
def printFirstLastName(first="", last=""):
    first = first.upper()
    last = last.upper()
    if not first and not last:
        print("You did not input any name")
    elif first and not last:
        print("Your name is {}".format(first))
    elif not first and last:
        print("Your last name is {}:".format(last))
    else:
        print("Your name is {} and your last name is {}".format(first, last))


ans1 = input("What's your name?")
ans2 = input("What's your surname?")

printFirstLastName(ans1, ans2)

