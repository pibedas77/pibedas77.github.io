# Acepting and Printing the inputs
# print(input("What is your name? "))

# Saving the user input
ans = input("What is your name? ")
print("Hello {}".format(ans))


ans1 = input("What is your name? ")
print("Hello {}!".format(ans1))

# working with user input to perform calculations
ans2 = input("Type a number to add: ")
print(type(ans2))  # Default type is string, it must be converted
result = 100 + int(ans2)
print(" 100 + {} = {}".format(ans2, result))

# Using Try and except Bolck
try:
    ans2 = input("Type a number to add: ")
    # print(type(ans2))  # Default type is string, it must be converted
    result = 100 + int(ans2)
    print(" 100 + {} = {}".format(ans2, result))
except:
    print("You did not pass a valid number...")

### Monday exercises ###
# 1.
ans = input("Write 'True'...")
ans = bool(ans)
float(ans)
print(type(ans))
# 2.
print("Let's play a game: pass me two numbers and I'll sum them for you")
try:
    ans = input("Insert your first value, please")
    ans2 = input("Insert your second number, please")
    result = int(ans) + int(ans2)
    print("Great, your result is: {}".format(result))
except:
    print("Sorry, you did not insert a number..")

# 3. Ask the user to insert year, make model and color of their car
print("I see you have a nice car...")
year = input("When was it produced?")
make = input("Which model is it?")
color = input("And... what color is it?")
result = print(
    "{} {} {}".format(year.capitalize(), color.capitalize(), make.capitalize())
)

## Tuesday ##
# If statements

# using an if statement to only run code if the condition is met
x, y = 5, 10
if x < y:
    print("x is less than y")

# check user input
ans = input("What is 5 + 5 ?")
if int(ans) == 10:
    print("You got it right!")

# using keyword 'and' in a if statement
x, y, z = 5, 10, 5
if x < y and x == z:
    print("Both statements are true")

# using keyword 'or' in a if statement
x, y, z = 5, 10, 5
if x < y or x != z:
    print("At least one statement is true")

# using keyword 'not' in a if statement
flag = False
if not flag:  # Same as saying "If is not true"
    print("Flag is false")

# using keyword 'in' in a if statement
word = "Baseball"
if "b" in word:  # Same as saying "If is not true"
    print("{} has a 'b'".format(word))

# using keyword 'not in' in a if statement
word = "Baseball"
if "x" not in word:  # Same as saying "If is not true"
    print("{} has no 'x'".format(word))

### Tuesday exercises ###
# Checking inclusion part 1
ans = input("Write any word...")
if "es" in ans:
    print("Your word has an 'es'...")
else:
    print("Your word does not have an 'es'...")

# Checking inclusion part 2
ans = input("Write any word...")
if ans[-3:] == "ing":
    print("Your word ends with 'ing'")
else:
    print("Your word '{}' does not end with 'ing'".format(ans))

# Checking equality
ans = input("insert a value and i will comapre it with you second value")
ans2 = input("Thanks, now insert your second value..")
if ans.lower() == ans2.lower():
    print("Your inputs match")
else:
    print("Your inputs do not match")

# Returning exponents
import math

ans = input("insert a number..")
ans = int(ans)
if ans < 10:
    result = math.sqrt(ans)
    print(result)
else:
    print("Your number is greater than 9")

### Tuesday exercises ###
## Elif Statements

x, y = 10, 10
if x < y:
    print("y is greater")
elif x > y:
    print("x is greater")
elif x == y:
    print("x is equal to y")

x, y, z = 10, 10, 11
if x < y:
    print("y is greater")
elif x > y:
    print("x is greater")
elif x == y:
    if x == z:
        print("x is equal to y, but also to z")
    elif x != z:
        print("x is equal to y, but NOT to z")

# A mayor difference between Elif statements against multiple If statements is:
# Elif is connected to one If statement, so only one condition is true and the rest do not run
# The following lines print both outputs
x, y, z = 10, 10, 11
if x == y:
    print("x is equal to y")
if x < z:
    print("z is greater than x")

# The following lines return only one output
# Because once one of the condition returns True the rest is not evaluated
x, y, z = 10, 10, 11
if x == y:
    print("x is equal to y")
elif x < z:
    print("z is greater than x")

## Wednesday exercise
# 1.
ans = int(input("Give me a number and I'll compare it with the number 100"))
if ans > 100:
    print("Your input is greater than 100")
elif ans < 100:
    print("Your input is smaller than 100")
else:
    print("Your input is equal to 100")

# 2.

x, y = 5, 10
if x > y:
    print("greater")
elif x < y:
    print("lower")

## Thursday ##
# Else statements

# It always needs to be associated with an if statement
# The Else Statement covers All others possibilities

name = "Jhon"
if name == "Jacob":
    print("Your name is Jacob")
else:
    print("Hello {} !".format(name))


name = "Mattia"
if name[0] == "A":
    print("Your name starts with 'A'")
elif name[0] == "B":
    print("Your name starts with 'B'")
elif name[0] == "J":
    print("Your name starts with 'J'")
else:
    print("Your name starts with {} !".format(name[0]))

## Thursday exercise
# 1. Fix the errors --> Output "Hello John"

name = "John"
if name == "Jack":
    print("Hello Jack")
else:
    print("Hello John")

# 2. User Input --> Ask the user the military time and
# base on it, return "Good Morning", ... , ...

time = int(input("What time is it?"))
if time < 1200:
    print("Good morning")
elif time >= 1200 and time < 1700:
    print("Good afternoon")
elif time >= 1700:
    print("Good evening")
else:
    print("I don't know")

## Friday ##
# Creating a calculator

# 1. Ask the user for the calculation they would like to perfermo
operation = input("What would you like to do: add/subtract/multiply/divide? ").lower()

# 2. ask for numbers
if operation == "subtract" or operation == "divide":
    print("You chose {}".format(operation))
    print("Please, keep in mind that the order of you number metter...")
num1 = input("What is your first number?")
num2 = input("What is your second numebr?")
print("First number {}; Second number {}".format(num1, num2))

# 3. Set Up Try and Except
try:
    num1, num2 = float(num1), float(num2)
    if operation == "add":
        result = num1 + num2
        print("{} + {} = {}".format(num1, num2, result))
    elif operation == "multiply":
        result = num1 * num2
        print("{} * {} = {}".format(num1, num2, result))
    elif operation == "subtract":
        result = num1 - num2
        print("{} - {} = {}".format(num1, num2, result))
    elif operation == "divide":
        result = num1 / num2
        print("{} / {} = {}".format(num1, num2, result))
    else:
        print("Sorry but {} is not an option".format(operation))
except:
    print("Improper numbers used. Please try againg")

# Weekly Challenge
# 2. Age Group
age = input("What is you age")
age = int(age)
if age > 0 and age <= 12:
    print("Kid")
elif age > 12 and age <= 19:
    print("Teenager")
elif age > 19 and age <= 30:
    print("Young adult")
elif age > 30 and age <= 64:
    print("Adult")
elif age > 64:
    print("Senior")
else:
    print("Sorry, i couldn't get it")
