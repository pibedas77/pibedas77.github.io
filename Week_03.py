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
