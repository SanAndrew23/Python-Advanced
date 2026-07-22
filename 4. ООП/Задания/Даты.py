class Date:
    def __init__(self, day=1, month=1, year=1970):
        self.day = day
        self.month = month
        self.year = year

    def set_from_str(self, date):
        date = date.split('.')
        self.day = int(date[0])
        self.month = int(date[1])
        self.year = int(date[2])

    def __str__(self):
        return f'{self.day}.{self.month}.{self.year}'

    def add_day(self):
        lst = [1, 3, 5, 7, 8, 9, 11]
        is_vis = (self.year % 100 != 0 and self.year % 4 == 0) or (self.year % 400 == 0)
        if self.month == 2:
            if is_vis:
                max_d = 29
            else:
                max_d = 28
        elif self.month in lst:
            max_d = 30
        else:
            max_d = 31
        self.day += 1
        if self.day >= max_d:
            self.day = 1
            self.month += 1
            if self.month > 12:
                self.month = 1
                self.year += 1
date = Date()
date.set_from_str('31.12.2028')
print(date)
date.add_day()
print(date)
