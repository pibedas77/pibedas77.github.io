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


def changePassword():
    email = input("To change password, enter you email: ").lower()
    password = input("Now, type your old password: ")
    clear_output
    with open("user.csv", mode="r+", newline="") as r:
        reader = csv.reader(r, delimiter=",")
        for row in reader:
            if row[0] == email and row[1] == password:
                print("We found you in our DB")
                newPassword = input("Type your new password: ")
                newPassword2 = input("Re-type you new password")
                if newPassword == newPassword2:
                    row[1] = newPassword
                    with open("user.csv", mode="w", newline="") as r:
                        writer = csv.writer(r, delimiter=",")
                        writer.writerow(row)
                    # print(row[0], row[1])
                    # wreader.writerows(row)
                    return True
    print("Something went wrong. Try again")
    return False


# Main loop
active = True
logged_in = False
while active:
    if logged_in:
        print("1. Logout | 2. Quit | 3. Change")
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
    elif choice == "change" and logged_in == True:
        changePassword()
    else:
        print("Sorry, try again later")
