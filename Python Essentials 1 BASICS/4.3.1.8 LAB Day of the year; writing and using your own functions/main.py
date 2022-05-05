def is_year_leap(year):
    condition = year%4 == 0 and (year%100 != 0 or year%100 == 0 and year%400 == 0)
    if condition: return True
    else: return False

def days_in_month(year, month):
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    is_leap = is_year_leap(year)
    bad_input = month > 12 or month <= 0
    if bad_input:
        return None
    if is_leap:
        days[11] = 29
    return days[month-1]

def day_of_year(year, month, day):
    is_leap = is_year_leap(year)
    # Bad day input handling
    if day > 0 and day < 32:
        if month == 2 and is_leap and day > 29:
            return print("February can't have more than 29 days")
        elif month == 2 and not is_leap and day > 28:
            return print("February in not leap year can't have more than 28 days")
    else: 
        return print("Wrong day input")
    
    # For computing: 1 = March, ..., 10 = December, 11 = Jan, 12 = Feb 
    # and Bad month input handling     
    if month < 13 and month > 2:
        month += 2
    elif month == 1 or month == 2:
        month += 10
    else: return None
    
    day_of_weak = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"] # 0 = Sunday, ...
    century = year // 100   # output 19 for 1987
    if month == 11 or month == 12:
        if year%100 == 0:
            y = 99
            century = year // 100 - 1
        else:
            y = year%100 - 1    # output 86 for 1987
    else: y = year%100    # output 87 for 1987

    a =  int(2.6 * month - 0.2)
    b = 2 * century + y
    c = int(y/4)
    d = int(century/4)
    
    W = (day + int(2.6 * month - 0.2) - 2 * century + y + int(y/4) + int(century/4))%7
#    print(day, "+", a, "-", b, "+", y, "+", c, "+", d, "%7 =", W)
    return day_of_weak[W]


print(day_of_year(2000, 2, 29))


