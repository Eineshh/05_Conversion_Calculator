# Checks user's choice is "time", "distance", or "weight"
def user_choice():
    # Lists of valid responses
    time_ok = ["s", "sec", "seconds", "min", "minutes", "hours", "h", "hour"]
    distance_ok = ["cm", "centimetres", "mm", "millimetres", "m", "metres", "km", "kilometres"]
    weight_ok = ["kg", "kilogram", "g", "gram", ]

    valid = False
    while not valid:

        # Ask user for choice and lowercase's it
        response = input("File Type: ").lower()

        # Checks for valid response
        if response in distance_ok:
            return "Distance"

        elif response in time_ok:
            return "Time"

        elif response in weight_ok:
            return "Weight"

        else:
            print("Please choose a valid File Type!")
            print()


# Main routine goes here
keep_going = ""
while keep_going == "":
    data_type = user_choice()
    print("You chose", data_type)
    print()
