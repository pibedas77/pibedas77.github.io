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
