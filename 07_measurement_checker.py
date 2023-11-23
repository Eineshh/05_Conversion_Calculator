def domain_check():
    error = "Please enter Weight, Distance or Time"

    # Loop start here
    while True:

        response = input("What domain? ").lower()

        if response == "time" or response == "t":
            return "Time"

        elif response == "weight" or response == "w":
            return "weight"

        elif response == "distance" or response == "d" or response == "length" or response == "l":
            return "distance"
        else:
            print(error)


# Main routine
domain = domain_check()
print("you chose", domain)
