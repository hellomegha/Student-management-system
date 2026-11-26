def get_valid_roll():

    while True:
        try:
            roll = int(input("Enter Roll Number: "))

            if roll <= 0:
                print("Roll Number must be greater than 0.")
            else:
                return roll

        except ValueError:
            print("Invalid Roll Number! Please enter a number.")


def get_valid_age():

    while True:
        try:
            age = int(input("Enter Age: "))

            if age <= 0:
                print("Age must be greater than 0.")
            else:
                return age

        except ValueError:
            print("Invalid Age! Please enter a number.")

def get_valid_name():

    while True:

        name = input("Enter Name: ")

        if name == "":
            print("Name cannot be empty.")

        elif name.replace(" ", "").isalpha():
            return name

        else:
            print("Name cannot contain numbers.")
