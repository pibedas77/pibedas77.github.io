# Friday: Creating user database with csv files

import csv
from IPython.display import clear_output


def registerUser():
    with open("user.csv", mode="a", newline="") as f:
        writer = csv.writer(f, delimiter=",")
        print("To register, please enter your info: ")
        email = input("Email: ")
        password = input("Password: ")
        password2 = input("Re-enter you password: ")
        clear_output
        if password == password2:
            writer.writerow([email, password])
            print("Your are now registered!")
        else:
            print("Something went wrong. Try again.")


def loginUser():
    print("To login, please enter your info:")
    email = input("Email: ")
    password = input("Password: ")
    clear_output
    with open("user.csv", mode="r") as f:
        reader = csv.reader(f, delimiter=",")
        for row in reader:
            if row == [email, password]:
                print("You are now logged in!")
                return True
    print("Something went wrong. Try again")
    return False


# Main loop
active = True
logged_in = False
while active:
    if logged_in:
        print("1. Logout | 2. Quit")
    else:
        print("1. Login | 2. Register | 3.Quit ")

    choice = input("What would you like to do?").lower()
    clear_output
    if choice == "register" and logged_in == False:
        registerUser()
    elif choice == "login" and logged_in == False:
        logged_in = loginUser()
    elif choice == "quit":
        active = False
        print("Thanks for using our software")
    elif choice == "logout" and logged_in == True:
        logged_in = False
        print("You are now logged out.")
    else:
        print("Sorry, try again later")


import csv

with open("user.csv", mode="r") as f:
    reader = csv.reader(f, delimiter=",")
    for row in reader:
        print(row)
