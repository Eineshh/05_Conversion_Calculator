def domain_check():
    error = "Please enter weight / distance or time"

    # loop start here
    while True:

        response = input("What domain? ").lower()

        if response == "time" or response == "t":
            return ("time")

        elif response == "weight" or response == "w":
            return ("weight")

        elif response == "distance" or response == "d" or response == "length" or response == "l":
            return ("distance")
        else:
            print(error)


# main routine``

domain = domain_check()
print("you chose", domain)


def ask_num():
    user_num = input("Please enter the integer (more than zero) you want to convert: ")


# Dictionaries


weight_dict = {
    "mg": 1000,
    "g": 1,
    "kg": 0.001,
}

distance_dict = {
    "mm": 1000,
    "cm": 100,
    "m": 1,
    "km": 0.001
}

time_dict = {
    "ms": 60000,
    "sec": 60,
    "min": 1,
    "hour": 0.6
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

        # output the value and the keyz

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
