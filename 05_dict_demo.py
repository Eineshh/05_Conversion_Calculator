my_dict = {
    "double": 2,
    "half": 0.5
}

num_check = int(input("Enter a number: "))
to_do = input("Double or Half?: ").lower()

# Find the value
multiply_by = my_dict[to_do]

# Work out the total
answer = num_check * multiply_by
print()
print("{} x {} = {}".format(num_check, multiply_by, answer))
