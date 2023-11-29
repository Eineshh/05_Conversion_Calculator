def conversion_checker():
    error = "Please chose valid measurement"

    # Loop
    while True:

        response = input("Which unit are you converting from: ").lower()

        if response == "mg" or response == "g" or response == "kg" or response == "t":
            return "weight"

        elif response == "sec" or response == "min" or response == "hour":
            return "time"

        elif response == "mm" or response == "cm" or response == "m" or response == "km":
            return "distance"
        else:
            print(error)


def unit_checker():
    error = "Please chose valid measurement"


    while True:

        response = input("Which unit are you converting to: ").lower()

        if response == "mg" or response == "g" or response == "kg" or response == "t":
            return "weight"

        elif response == "sec" or response == "min" or response == "hour":
            return "time"

        elif response == "mm" or response == "cm" or response == "m" or response == "km":
            return 'distance'
        else:
            print(error)


# main routine

conversion = conversion_checker()
print("you converting from", conversion)
unit = unit_checker()
print("to", unit)
