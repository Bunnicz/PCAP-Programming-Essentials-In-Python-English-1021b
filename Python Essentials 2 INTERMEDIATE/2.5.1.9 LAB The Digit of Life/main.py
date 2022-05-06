# The Digit of Life
def calc_sum(date):
    """Takes in string with birthday and returns sum of every digit"""
    sum = 0
    for i in date:
        sum += int(i)
    return sum


while True:
    date = input("Write your birthday (format YYYYMMDD, or YYYYDDMM, or MMDDYYYY): ")
    date = date.strip()

    if date.isdigit():
        break
    else:
        print("Wrong input: Try again!")

digit_of_life = calc_sum(date)

while digit_of_life >= 10:
    digit_of_life = calc_sum(str(digit_of_life))

print("Your digit of life is", digit_of_life)
