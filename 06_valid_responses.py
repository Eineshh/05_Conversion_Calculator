# checks user choice is 'distance', 'time' or 'weight'
def user_choice():
    # list of valid responses
    distance_ok = ["mm", "millimeters", "millimetres", "cm", "centimetres", "centimeters", "m", "metres", "meters",
                   "km", "kilometers", "kilometres"]
    time_ok = ["sec", "seconds", "s", "min", "minutes", "m", "hr", "hours", "h"]
    weight_ok = ["g", "gram", "kg", "kilogram"]

    valid = False
    while not valid:

        # ask user for choice and change response to lowercase
        response = input("file type (Distance / Time / Weight): ").lower()

        # Checks for valid response and returns text, integer or image

        if response in distance_ok:
            return "distance"

        elif response in time_ok:
            return "time"

        elif response in weight_ok:
            return "weight"

        else:
            print("please choose a valid response!")
            print()


# Main routine goes here
keep_going = ""
while keep_going == "":
    data_type = user_choice()
    print("You chose", data_type)

    print()