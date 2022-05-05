def is_year_leap(year):
    condition = year%4 == 0 and (year%100 != 0 or year%100 == 0 and year%400 == 0)
    if condition: return True
    else: return False

def days_in_month(year, month):
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    is_leap = is_year_leap(year)
    if month <= 0 or month >= 13:
        return None
    if is_leap:
        days[1] = 29
        return days[month-1]
    else:
        return days[month-1]

test_years = [1900, 2000, 2016, 1987, 2022, 13]
test_months = [2, 2, 1, 11, 0, 14]
test_results = [28, 29, 31, 30, None, None]
for i in range(len(test_years)):
	yr = test_years[i]
	mo = test_months[i]
	print(yr, mo, "-> ", end="")
	result = days_in_month(yr, mo)
	if result == test_results[i]:
		print("OK")
	else:
		print("Failed")
