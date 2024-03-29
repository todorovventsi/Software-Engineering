class take_skip:
    def __init__(self, step, count):
        self.step = step
        self.count = count
        self.start = 0
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.counter < self.count:
            value = self.start
            self.start += self.step
            self.counter += 1
            return value
        raise StopIteration


numbers = take_skip(10, 5)
for number in numbers:
    print(number)
