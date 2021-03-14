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

# Wednesday: While Loops
# While loops are generally used to loop based on a condition rather than counting
health = 10
while health > 0:
    print(health)
    health -= 1

# Nested loops
for i in range(3):
    for j in range(4):
        print(i, j)

# Wednesday exercises
# 1. User Input:
ans = input("Give me a number and I'll write it. Write Quit to 'quit' the prograg")
while ans != "quit":
    print(ans)
    ans = input("Give me a number and I'll write it. Write Quit to 'quit' the prograg")
# 2. Double Loop
game_over = False
while not game_over:
    for i in range(5):
        print(i)
        if i == 2:
            game_over = True
            break

# Thursday: working with lists
nums = [5, 10, 15]
length = len(nums)
print(length)
print(nums[1:3])
print(nums[:2])
print(nums[::2])
print(nums[-2:])

# Adding items to a list
# append() add a value to the back of a list
nums = [4, 8]
nums.append(12)
print(nums)

# insert() needs an index to insert a value to a specific location
words = ["hello", "ciao"]
words.insert(0, "hola")
print(words)

# Removing items
# pop() removes the last item from a list. You can also specify an index
# in order to remove a value from a specific position.
# pop() also returns the value that has been deleted
items = ["Tizio", "ciao", "Caio"]
items.pop()
item_removed = items.pop(0)
print(item_removed, "\n", items)

# remove()
sports = ["baseball", "football", "soccer", "hockey"]
try:
    sports.remove("socc")
    print("The item has been removed")
except:
    print("The item does not exit in the list")

# Working with numerical list data
num = [2, 3, 5, 10]
print(min(num))
print(max(num))
print(sum(num))

# Sorting a list
# it is usefull to sort lists and there are a few methods in Python
# sorted()
nums = [5, 10, 0, 3]
sorted_nums = sorted(nums)
print(nums, "\t", sorted_nums)

# sort() will change the original list directly
nums = [5, 10, 0, 3]
print(nums)
nums.sort()
print(nums)

# Conditionals and lists
names = ["Jack", "Robert", "Mary"]
if "Mary" in names:
    print("found")
if "Jimmy" not in names:
    print("not found")

# Checking an empty list
nums = []
if not nums:  # we can also write "if nums == []"
    print("empty")

# Checking a not empty list
nums = [1, 2, 3]
if nums:
    print("not empty")

# It is possible to use both loops to iterate a list
sports = ["baseball", "football", "soccer", "hockey"]
for sport in sports:  # NOTE sport is a temporary variable
    print(sport)

names = ["Bob", "Jack", "Robert", "Mary", "Bob", "Ervin"]
while "Bob" in names:
    names.remove("Bob")
print(names)


# Thursday Exercise
# 1. Remove duplicates using the count() method
names = ["Bob", "Kenny", "Amanda", "Bob", "Kenny"]
for i in names:
    if names.count(i) > 1:
        names.remove(i)
print(names)


# 2. User input: use a while loop tp continually ask the user to input a word until they type "quit"
lst = []
ans = ""
while ans != "quit":
    ans = input("Write a string")
    if ans != "quit":
        lst.append(ans)
        # print(lst)
for l in lst:
    print(l)

## Friday: Creating Hangman
# Adding imports
from random import choice
from IPython.display import clear_output

# declare variables
words = ["tree", "basket", "chair", "paper", "python"]
word = choice(words)
guessed, lives, game_over = [], 7, False

guesses = ["_ "] * len(word)

# creating main loop
while not game_over:
    hidden_word = "".join(guesses)
    print("Your guessed word: {}".format(guessed))
    print("Word to guess {}".format(hidden_word))
    print("Lives : {}".format(lives))
    #    print(word)
    #    print("".join(guesses))
    ans = input("Type quit or guess a letter: ").lower()
    clear_output()
    if ans == "quit":
        print("Thanks for playing. ")
        game_over = True
    elif word == "".join(guesses):
        print("Congrats, you have guessed correctly!")
        game_over = True
    elif ans in word and ans not in guessed:
        print("You've gueesed correctly!")
        for i in range(len(word)):
            if word[i] == ans:
                guesses[i] = ans
    elif ans in guessed:
        print("You've already guessed that. Try agin.")
    else:
        lives -= 1
        print("Incorrect. You have lost a life.")
        if ans not in guessed:
            guessed.append(ans)
        if lives <= 0:
            print("You have lost all you lives. Game over!")
            game_over = True


## Weekly challenges
# 1. Piramids

ans = input("insert a number...")
end = int(ans)
start = int(1)
for i in range(start, end):
    print(" " * end, "x" * start, "x" * start, sep="")
    end = end - 1
    start = start + 1

end = input("insert a number...")
end = int(end)
start = int(1)
for i in range(start, end):
    print(" " * end, " x" * start)
    end = end - 1
    start = start + 1

# 2. Output names

names = ["Jhon", "    ", "Amanda", "tst"]
vowels = "aeiou"
for i in names:
    for vowel in vowels:
        if vowel in i:
            print(i)
        else:
            continue

# 3. Convert Celsius
temps = [32, 12, 44, 29]
for t in temps:
    conversion = (9 / 5) * t + 32
    print(conversion)
