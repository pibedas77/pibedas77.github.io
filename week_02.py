x = 3
y = 10
result = x + y

print(str(x) + " + " + str(y) + " = " + str(result))


x = 245.54
y = 13.66
result = x * y
print(result)

# .format
name = "Camille"
age = 33
print("Hello {} I konw your age is {}".format(name, age))

# f Strings
name = "Camille"
age = 33
print(f"Hello {name} I konw your age is {age}")


word = "Hello"
print(word[1])
print(word[-1])


# Slices --> il primo parametro indica l'inizio, il secondo la fine, mentre il terzo è opzionale e indica la riccorrenza
word = "Hello"
print(word[0:3])

# Wednesday Exercise 1
age = 23
cash = 4.5
bolean = False
name = "Jhon"
print(f"{age} {cash} {bolean} {name}")
print("{} {} {} {}".format(age, cash, bolean, name))
# Exercise 2

name = "Mattia"
hobby = "football"
program_name = "Python"
print("{}'s favourite activity is {}".format(name, hobby))
print("{} is working on {} programming".format(name, program_name))

# Thursday - Manipulating Strings
name = "mattia"
surname = "pivetta"
fullname = name + " " + surname
print(fullname.upper())

name = "mattia"
surname = "pivetta"
fullname = name + " " + surname + " " + "!"
print(fullname.replace("!", "?"))

s = "Look over that way"
print(s.find("over"))

s = "   Look over that way  "
print(s.strip())

s = "This words are splitted by spaces"
print(s.split())


s = "$$$Look over that way  "
print(s.rstrip(" $"))

help(" ".strip)


# # Friday Challenge: Create a Receipt Printing Program
# Defining Variables

p1_nanme, p1_price = "Books", 49.95
p2_nanme, p2_price = "Computer", 579.99
p3_nanme, p3_price = "Monitor", 124.89

# Create company name and info
company_name = "conding tample, inc."
company_address = "283 Frankling St."
company_city = "Boston, MA"

# Declare Ending Message
message = "Thanks for shopping with us today!"

# Create top border
print("*" * 50)

# Print company info by using format
print("\t\t{}".format(company_name.title()))
print("\t\t{}".format(company_address))
print("\t\t{}".format(company_city))

# Print line between sections
print("-" * 50)
# Print out header for section of itmes
print("\tProdict Name \tProdict Price")

# Create a print statement for eache product
print("\t{}\t\t${}".format(p1_nanme.title(), p1_price))
print("\t{}\t${}".format(p2_nanme.title(), p2_price))
print("\t{}\t\t${}".format(p3_nanme.title(), p3_price))

# Print line between sections
print("=" * 50)

# Print out headers for Total section
print("\t\t\tTotal")

# Calculate total and print out
total = p1_price + p2_price + p3_price
print("\t\t\t${}".format(total))

# Print a line between sections
print("=" * 50)

# output ending line
print("\n\t{}\n".format(message))

# create bottom line
print("*" * 50)

# # Friday Challenge: Create a Receipt Printing Program
# Defining Variables

p1_nanme, p1_price = "Books", 49.95
p2_nanme, p2_price = "Computer", 579.99
p3_nanme, p3_price = "Monitor", 124.89

# Create company name and info
company_name = "conding tample, inc."
company_address = "283 Frankling St."
company_city = "Boston, MA"

# Declare Ending Message
message = "Thanks for shopping with us today!"

# Create top border
print("*" * 50)

# Print company info by using format
print("*\t\t{}\t\t *".format(company_name.title()))
print("*\t\t{}\t\t *".format(company_address))
print("*\t\t{}\t\t\t *".format(company_city))

# Print line between sections
print("-" * 50)
# Print out header for section of itmes
print("*\tProdict Name \tProduct Pricet\t\t *")

# Create a print statement for eache product
print("*\t{}\t\t${}\t\t\t *".format(p1_nanme.title(), p1_price))
print("*\t{}\t${}\t\t\t *".format(p2_nanme.title(), p2_price))
print("*\t{}\t\t${}\t\t\t *".format(p3_nanme.title(), p3_price))

# Print line between sections
print("=" * 50)

# Print out headers for Total section
print("*\t\t\tTotal\t\t\t *")

# Calculate total and print out
total = p1_price + p2_price + p3_price
print("*\t\t\t${}\t\t\t *".format(total))

# Print a line between sections
print("=" * 50)

# output ending line
print("*\t\t\t\t\t\t *\n*\t{}\t *\n*\t\t\t\t\t\t *".format(message))

# create bottom line
print("*" * 50)
