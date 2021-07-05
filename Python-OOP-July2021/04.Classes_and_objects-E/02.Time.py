"""
1 min = 60s
1 hour = 3600s

"""


class Time:
    max_hours = 23
    max_minutes = 59
    max_seconds = 59

    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def set_time(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def get_time(self):
        return f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"

    def next_second(self):
        self.seconds += 1
        if self.seconds == 60:
            self.seconds = 00
            self.minutes += 1
            if self.minutes == 60:
                self.minutes = 00
                self.hours += 1
                if self.hours == 24:
                    self.hours = 00
        return self.get_time()


time = Time(23, 59, 59)
print(time.next_second())
