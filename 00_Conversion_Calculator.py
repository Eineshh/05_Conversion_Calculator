# Functions go here

def statement_generator(text, decoration):
    # Make string with five characters
    ends = decoration * 5

    # add decoration to start and end of statement
    statement = "{} {} {}".format(ends, text, ends)

    print()
    print(statement)
    print()

    return ""


# displays instructions / information
def instructions():
    statement_generator("Instructions / Information", "=")
    print()
    print("Please choose a unit to convert from and a unit to convert to")
    print()
    print("This program converts measurements of time, mass, and distance")
    print()
    print("Complete as many calculations as necessary, pressing <enter> at the end of each calculation or any key to "
          "quit")
    print()
    return ""


# checks input is a number more than given value

def num_check(question):
    valid = False
    while not valid:
        print()
        error = "Please enter an integer that is more than or equal to zero"

        try:

            low_num = 1

            # Ask user to enter a number
            response = int(input(question))

            # checks number is more than zero or under 200
            if low_num <= response:
                return response

            # outputs error if input is invalid
            else:
                print(error)
                print()

        except ValueError:
            print(error)


# Checks user choice is 'weight', 'distance' or 'time'
def user_choice():
    valid = False
    while not valid:

        # ask user for choice and change response to lowercase
        response = input("measurement (weight / distance / time): ").lower()

        # if they choose "t" or "text" or "txt", return "text"
        weight_ok = ["weight", "w", "wt"]
        if response in weight_ok:
            return "weight"

        # if they choose "int" or "integer", return "integer"
        distance_ok = ["distance", "length", "d", "dist"]
        if response in distance_ok:
            return "distance"

        # if they choose "image" or "p" or "img", return "image"
        time_ok = ["time", "t"]
        if response in time_ok:
            return "time"
        else:
            print("Please choose a valid measurement!")
            print()


def ask_num():
    input("Please enter the integer (more than zero) you want to convert: ")


# Dictionaries


weight_dict = {
    "mg": 1000,
    "g": 1,
    "kg": 0.001,
    "t": 0.000001
}

distance_dict = {
    "cm": 100,
    "m": 1,
    "km": 0.001,
    "mm": 1000
}

time_dict = {
    "sec": 60,
    "min": 1,
    "hour": 0.6,
    "day": 0.000694444,
    "ms": 60000
}


def weight_conv():
    # Ask user what to convert from and to

    weight_from = input("Enter unit to convert from (mg, g, kg, t): ")
    print()
    weight_to = input("Enter unit to convert to (mg, g, kg, t): ")
    print()

    weight_amount = float(input("Please enter the amount you want to convert: "))

    if weight_from in weight_dict:
        # find the answer
        divide_by = weight_dict[weight_from]

        part_1 = weight_amount / divide_by
        factor_1 = weight_dict[weight_to]

        weight_answer = part_1 * factor_1

        # output the value and the key

        print("{}{} = {}{}".format(weight_amount, weight_from, weight_answer, weight_to))


def distance_conv():
    # Ask user what to convert from and to

    distance_from = input("Enter unit to convert from (mm, cm, m, km): ")
    print()
    distance_to = input("Enter unit to convert to (mm, cm, m, km): ")
    print()

    distance_amount = float(input("Please enter the amount you want to convert: "))

    if distance_from in distance_dict:
        # find the answer
        divide_by = distance_dict[distance_from]

        part_1 = distance_amount / divide_by
        factor_1 = distance_dict[distance_to]

        distance_answer = part_1 * factor_1

        # output the value and the key

        print("{}{} = {}{}".format(distance_amount, distance_from, distance_answer, distance_to))


def time_conv():
    # Ask user what to convert from and to

    time_from = input("Enter unit to convert from (mm, cm, m, km): ")
    print()
    time_to = input("Enter unit to convert to (mm, cm, m, km): ")
    print()

    time_amount = float(input("Please enter the amount you want to convert: "))

    if time_from in time_dict:
        # find the answer
        divide_by = time_dict[time_from]

        part_1 = time_amount / divide_by
        factor_1 = time_dict[time_to]

        time_answer = part_1 * factor_1

        # output the value and the key

        print("{}{} = {}{}".format(time_amount, time_from, time_answer, time_to))


# Main Routine goes here

# Heading
statement_generator("Conversion Calculator for Weight, Distance & Time", "*")

# Display instructions if user has not used the program before
first_time = input("Press <enter> to see the instructions or any key to continue: ")
print()

if first_time == "":
    instructions()

# Loop to allow multiple calculation's per session
keep_going = ""
while keep_going == "":

    # Ask the user for the file type
    data_type = user_choice()
    print("You chose", data_type)

    # For integers, ask for integer
    # (must be an integer more than / equal to 0)
    if data_type == "weight":
        weight_conv()

    # For images, ask for width and height
    # (must be integers more than / equal to 1)
    elif data_type == "distance":
        distance_conv()

    # For text, ask for a string
    else:
        time_conv()

print()
keep_going = input("Press <enter> to continue or any key to quit ")
print()
