## Lists
# Declaring a list of values

nums = [1, 2, 3, 5, 20]
print(nums)


print(nums[1])


num = 3
data = [True, "test", num]
print(data)


# Lists within lists

data = [5, "book", [34, "hello"], True]
print(data)
print(data[2])
# Access lists within lists. you can do it by using double bracket notation
print(data[2][0])

inner_list = data[2]
print(inner_list)
print(inner_list[1])

# Also strings can be index further
data = [5, "book", [34, "hello"], True]
print(data[1][0])

# Changing values in a Lists through index
data = [5, 10, 15, 20]
print(data)
data[0] = 100  # It enables to change data at index 0

print(data)

# Variable storage
a = [5, 10]
print(id(a))  # It shows the variable's ID
# that enables the item to have its own location

# In this case we see that the following two variables  share the same location
# Because so, when changing variable a, also b will change
a = [5, 10]
b = a
print("a: {} \b b: {}".format(a, b))
print("Location a[0]: {} \t Location b[0]: {}".format(id(a[0]), id(b[0])))
a[0] = 20
print("a: {} \t b: {}".format(a, b))

b[0] = 200
print("a: {} \t b: {}".format(a, b))
# In fact, when two variables share the same memory location, when you change one of them, you change both.

# In order to create a similar list, without altering the original, you just need to copy it
# [:] enables to copy a list!
data = [5, 10, 15, 20]
data_copy = data[:]
data[0] = 50
print("data: {} \t data_copy: {}".format(data, data_copy))
print("Location a[0]: {} \t Location b[0]: {}".format(id(data), id(data_copy)))

# Monday exercise
# 1. Sports:
sports = ["football", "golf", "racing", "bowling", "ski"]
print("I really like to play {}".format(sports[0]))

# 2. First character
names = ["Jhon", "Abraham", "Sam", "Kelly"]
print(
    "'{}', '{}', '{}', '{}'".format(names[0][0], names[1][0], names[2][0], names[3][0])
)

# Tuesday: For Loops
# Loops are usefull to rerun the same lines of code several times.
# Lopps will always run untill a condition is met

for num in range(5):
    print("Value: {}".format(num))
# ! Range() function allows to count from one number to another.
# With in the function we are also able to define where to start and end and how much we increment or decrement

for num in range(2, 10, 2):
    print("Value: {}".format(num))

# Looping by element
# When working with data types that are iterable, we can use them in a for loop

name = "Mattia Pivetta"
for letter in name:
    print("Value: {}".format(letter))

# Continue statement
# Once a continue statement is hit, the current iteration stops and goes back to the top loop

for num in range(5):
    if num == 3:
        continue  # when num == 3, stop current iteratione and go back to the looping
    print(num)


# Break statement
# This is one of the most important statements. It allows us to break out of a loop at any point in time.
# This is usefull for stopping a loop when a condition is met
for num in range(5):
    if num == 3:
        break
    print("Value: {}".format(num))

# Pass statement
# Pass is a just a placeholder so that the program doesn't break
for i in range(5):
    # TO-DO: Add code to print
    pass

# Tuesday exercises
# 1. Divisible by Three
for i in range(3, 100, 3):
    print("Value: {}".format(i))

# 2. Only Vowels
ans = input("Write a word")
for i in ans:
    if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
        print(i)

ans = input("Write a word")
for ans in ("a", "e", "i", "o", "u"):
    print(ans)
