from datetime import datetime

# November 4, 2020 , 14:53:00
dt = datetime(2020, 11, 4, 14, 53, 0)
# print(dt)
print(dt.strftime("%Y/%m/%d %H:%M:%S"))
print(dt.strftime("%Y/%B/%d %H:%M:%S %p"))
print(dt.strftime("%a, %Y %b %d"))
print(dt.strftime("%A, %Y %B %d"))
print(dt.strftime("Weekday: %w"))
print(dt.strftime("Day of the year: %j"))
print(dt.strftime("Week number of the year: %U"))
