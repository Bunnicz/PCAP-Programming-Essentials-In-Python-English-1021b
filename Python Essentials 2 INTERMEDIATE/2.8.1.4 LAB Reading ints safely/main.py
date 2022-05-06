def read_int(prompt, min, max):
    # takes string prompt and min-max range and returns valid input
    while True:
        try:
            inp = int(input(prompt))
            if min <= inp <= max:
                break
            else:
                assert min <= inp <= max
        except ValueError:
            print("Error: wrong input")
        except AssertionError:
            print(f"Error: the value is not within permitted range ({min}..{max})")
    return inp


v = read_int("Enter a number from -10 to 10: ", -10, 10)

print("The number is:", v)
