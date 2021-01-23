# Acepting and Printing the inputs
# print(input("What is your name? "))

# Saving the user input
ans = input("What is your name? ")
print("Hello {}".format(ans))


ans = input("What is your name? ")
print("Hello {}!".format(ans))

# working with user input to perform calculations
ans = input("Type a number to add: ")
print(type(ans))  # Default type is string, it must be converted
result = 100 + int(ans)
print(" 100 + {} = {}".format(ans, result))
