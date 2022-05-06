class WeekDayError(Exception):
    pass


class Weeker:
    def __init__(self, day):
        self.DayOfWeek = ("Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun")
        self.day = day
        if self.day not in self.DayOfWeek:
            raise WeekDayError
        self.RestOfWeek = None
        self.NewDay = None
        self.index = self.DayOfWeek.index(self.day)

    def __str__(self):
        if self.NewDay is not None:
            return self.NewDay
        else: return self.day

    def add_days(self, n):
        self.RestOfWeek = n % 7
        self.NewDay = self.DayOfWeek[self.index + self.RestOfWeek]

    def subtract_days(self, n):
        self.RestOfWeek = n % 7
        self.NewDay = self.DayOfWeek[self.index - self.RestOfWeek]


try:
    weekday = Weeker('Mon')
    print(weekday)
    weekday.add_days(15)
    print(weekday)
    weekday.subtract_days(23)
    print(weekday)
    weekday = Weeker('Monday')
except WeekDayError:
    print("Sorry, I can't serve your request.")
