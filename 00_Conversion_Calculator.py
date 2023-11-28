# Functions go here

def statement_generator(text, decoration):
    # Make string with five characters
    ends = decoration * 5

    # Add decoration to start and end of statement
    statement = "{} {} {}".format(ends, text, ends)

    print()
    print(statement)
    print()

    return ""


# Display Instructions

def instructions():
    statement_generator("Instructions / Information", "-" * 8)
    print("Please choose a unit to convert to and from!")
    print()
    print("This program converts time, distance and weight to other measurements")
    print()
    print("Complete as many calculations as necessary, pressing <enter> at the end of each calculation or any key to "
          "quit")
    print("-" * 111)
    print()
    return ""


# Checks input is a number more than given value
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
            print()


# Checks user choice is either "time, "distance", or "weight",
def user_choice():
    valid = False
    while not valid:

        # Ask user for measurement
        response = input("Measurement (Time, Distance or Weight): ").lower()

        # If "w" is chosen, return "weight"
        weight_ok = ["weight", "w", "wt"]
        if response in weight_ok:
            return "Weight"

        # If "d" is chosen, return "distance"
        distance_ok = ["distance", "d"]
        if response in distance_ok:
            return "Distance"

        # If "t" is chosen, return "time"
        time_ok = ["time", "t"]
        if response in time_ok:
            return "Time"
        else:
            print("Please choose a valid measurement!")
            print()


def ask_num():
    input("Please enter an integer (more than or equal to 0): ")


def weight_conv():
    # Ask user what to convert from and to
    weight_from = input("Enter a unit to convert from: ")
    print()
    weight_to = input("Enter unit to convert to: ")
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

    time_from = input("Enter unit to convert from: ")
    print()
    time_to = input("Enter unit to convert to: ")
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

# Dictionary

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


# Heading
statement_generator("Conversion Calculator for Weight, Distance & Time", "⋆" * 4)

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
    print()

    # Weight
    if data_type == "weight":
        weight_conv()

    # Distance
    elif data_type == "distance":
        distance_conv()

    # Time
    else:
        time_conv()

    from_unit = input("what unit do you have? ")
    amount = num_check(f"How many {from_unit} do you have?")
    to_unit = input("What do you want to convert to? ")

    # Find the value
    multiply_by = num_check,

    # Work out the total
    answer = num_check * multiply_by

    print()
    print("{} x {} = {}".format(num_check, multiply_by, answer))


print()
keep_going = input("Press <enter> to continue or any key to quit: ")
print()
