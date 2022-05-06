import calendar


class MyCalendar(calendar.Calendar):
    def __init__(self, year=1970, weekday=0):
        calendar.Calendar.__init__(self)
        self.weekday = weekday
        self.year = year
        if not 0 <= weekday < 7:
            raise ValueError

    def count_weekday_in_year(self):
        count = 0
        for i in range(1, 13):
            data = self.monthdays2calendar(self.year, i)
            for week in data:
                for day in week:
                    if day[1] == self.weekday and day[0] != 0:
                        count += 1
        return print(count)


cal = MyCalendar(2019, 0)
cal.count_weekday_in_year()
cal1 = MyCalendar(2000, 6)
cal1.count_weekday_in_year()

print([[c for c in range(r)] for r in range(3)])
print(cal)