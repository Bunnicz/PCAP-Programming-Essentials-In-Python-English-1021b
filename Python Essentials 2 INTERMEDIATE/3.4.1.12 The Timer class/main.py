class Timer:
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def __str__(self):
        hour = self.hours
        minute = self.minutes
        second = self.seconds
        if self.hours < 10:
            hour = "0" + str(self.hours)
        if self.minutes < 10:
            minute = "0" + str(self.minutes)
        if self.seconds < 10:
            second = "0" + str(self.seconds)
        string = f'{hour}:{minute}:{second}'
        return string

    def next_second(self):
        self.seconds += 1
        if self.seconds > 59:
            self.seconds = 0
            self.minutes += 1
        if self.minutes > 59:
            self.minutes = 0
            self.hours += 1
        if self.hours > 23:
            self.hours = 0

    def prev_second(self):
        self.seconds -= 1
        if self.seconds < 0:
            self.seconds = 59
            self.minutes -= 1
        if self.minutes < 0:
            self.minutes = 59
            self.hours -= 1
        if self.hours < 0:
            self.hours = 23


timer = Timer(23, 59, 59)
print(timer)
timer.next_second()
print(timer)
timer.prev_second()
print(timer)
