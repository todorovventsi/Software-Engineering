class countdown_iterator:
    def __init__(self, count):
        self.count = count
        self.stop_count = 0

    def __iter__(self):
        return self

    def __next__(self):
        value = self.count
        while self.count >= self.stop_count:
            self.count -= 1
            return value
        raise StopIteration


iterator = countdown_iterator(10)
for item in iterator:
    print(item, end=" ")
