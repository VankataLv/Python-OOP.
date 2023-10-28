class Time:
    max_hours = 23
    max_minutes = 59
    max_seconds = 59

    def __init__(self, hours: int, minutes: int, seconds: int):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def set_time(self, hours: int, minutes: int, seconds: int):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def get_time(self) -> str:
        return f"{self.hours:02}:{self.minutes:02}:{self.seconds:02}"

    def next_second(self):
        if self.seconds == Time.max_seconds:
            if self.minutes == Time.max_minutes:
                if self.hours == Time.max_hours:
                    self.seconds = 0
                    self.minutes = 0
                    self.hours = 0
                else:
                    self.seconds = 0
                    self.minutes = 0
                    self.hours += 1
            else:
                self.seconds = 0
                self.minutes += 1

        else:
            self.seconds += 1

        return Time.get_time(self)

# time = Time(9, 30, 59)
# print(time.next_second())

# time = Time(10, 59, 59)
# print(time.next_second())

time = Time(23, 59, 59)
print(time.next_second())