# Functions go here

# Puts a series of symbols at start and end of text
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
    print("Please choose a unit to convert to and from")
    print()
    print("This program is able to covert units such as Weight, Distance and Time!")
    print()
    print("Complete as many calculations as necessary, pressing <enter> at the end of each calculation or any key to "
          "quit")
    print("-" * 111)
    print()
    return ""


# Checks input is a number more than a given value
def num_check(question):
    # Checks that input is more than zero
    valid = False
    while not valid:
        
        error = "Please enter an integer that is more than zero"

        try:
        
            low_num = 1
            
            # Ask user to enter a number
            response = int(input(question))
            
            # Checks number is more than zero
            if low_num <= response:
                return response

            # Outputs error if input is invalid
            else: 
                print(error)
                print()

        except ValueError:
            print(error)
            print()


# Checks user choise is either "weight", "distance" or "time""
def user_choice():

    valid = False
    while not valid:
        
        # Get user input and change it to lowercase
        response = input("Value (Weight, Distance or Time): ").lower()

        # If "w" or "weight" is chosen, return "weight"
        weight_ok = ["weight", "w",]
        if response in weight_ok:
            return "weight"

        # If "d", "length" or "distance" is chosen, return "distance"
        distance_ok = ["distance", "length", "d",]
        if response in distance_ok:
            return "distance"

        # If "t" or "time" is chosen, return "time"
        time_ok = ["time", "t"]
        if response in time_ok:
            return "time"

        else: 
            print("Please choose a valid measurement!")
            print()

def ask_num():

    user_num = input("Please enter the integer you'd like to convert (more than zero): ")

def weight_conv():
    
    # Ask user for input
    weight_amount = float(input("Value for Conversion: "))
    
    weight_from = input("Current Unit (mg, g, kg, t): ")
    print()
    weight_to = input("Unit for Conversion (mg, g, kg, t): ")
    print()


    if weight_from in weight_dict:

            # Calculates the answer
            divide_by = weight_dict[weight_from]

            part_1 = weight_amount / divide_by 
            factor_1 = weight_dict[weight_to]

            weight_answer = part_1 * factor_1

            # Outputs input and answer
            print("{}{} = {}{}".format(weight_amount, weight_from, weight_answer, weight_to))
        


def distance_conv():

    # Ask user for input
    distance_amount = float(input("Value for Conversion: "))
    
    distance_from = input("Current Unit (mm, cm, m, km): ")
    print()
    distance_to = input("Unit for Conversion (mm, cm, m, km): ")
    print()


    if distance_from in distance_dict:
        

            # Calculates the answer
            divide_by = distance_dict[distance_from]

            part_1 = distance_amount / divide_by 
            factor_1 = distance_dict[distance_to]

            distance_answer = part_1 * factor_1

            # Outputs input and answer
            print("{}{} = {}{}".format(distance_amount, distance_from, distance_answer, distance_to))


def time_conv():

    # Ask user for input
    time_amount = float(input("Value for Conversion: "))
    
    time_from = input("Current Unit (ms, s, m, hr, d): ")
    print()
    time_to = input("Unit for Conversion (ms, s, m, hr, d: ")
    print()


    if time_from in time_dict:
        

            # Calculates the answer
            divide_by = time_dict[time_from]

            part_1 = time_amount / divide_by 
            factor_1 = time_dict[time_to]

            time_answer = part_1 * factor_1
            

            # Outputs the input and answer
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
    "km":0.001,
    "mm": 1000
    }

time_dict = {
    "s": 60,
    "m": 1, 
    "hr": 0.6,
    "d": 0.000694444,
    "ms": 60000
    }

# Heading
statement_generator("Conversion Calculator for Weight, Distance & Time", "⋆" * 4)

# Display instructions if user has not used the calculator before
first_time = input("Press <enter> to see the instructions or any key to continue: ")
print()
if first_time == "":
    instructions()
    
# Loop to allow multiple calculations per session
keep_going = ""
while keep_going == "":

    # Ask the user for input
    data_type = user_choice()
    print("You chose", data_type)
    print()

    # Converts weight
    if data_type =="weight":
        weight_conv()
    
    # Converts distance
    elif data_type =="distance":
        distance_conv()

    # Converts time
    else:
        time_conv()

    print()
    keep_going = input("Press <enter> to continue or any key to quit: ")
    print()
    
print()
print("Thank you for using the Conversion Calculator :)")
