# 4.3.1.7 LAB: How many days: writing and using your own functions

LAB

Estimated time
15-20 minutes

Level of difficulty
Medium

Prerequisites
LAB 4.3.1.6

Objectives

Familiarize the student with:

- projecting and writing parameterized functions;
- utilizing the return statement;
- utilizing the student's own functions.

## Scenario

Your task is to write and test a function which takes two arguments (a year and a month) and returns the number of days for the given month/year pair (while only February is sensitive to the year value, your function should be universal).

The initial part of the function is ready. Now, convince the function to return None if its arguments don't make sense.

Of course, you can (and should) use the previously written and tested function (LAB 4.3.1.6). It may be very helpful. We encourage you to use a list filled with the months' lengths. You can create it inside the function - this trick will significantly shorten the code.

We've prepared a testing code. Expand it to include more test cases.
```
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
```
