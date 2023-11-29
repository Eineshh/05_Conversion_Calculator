# Puts series of symbols at start and end of text (for emphasis)
def statement_generator(text, decoration):
    # Make string with five character
    ends = decoration * 5

    # add decoration to start and end of statement
    statement = "{}  {}  {}".format(ends, text, ends)

    print()
    print(statement)
    print()

    return ""


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
