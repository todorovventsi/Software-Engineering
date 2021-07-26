class custom_range:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        while self.start <= self.end:
            temp = self.start
            self.start += 1
            return temp
        raise StopIteration
        # if self.start > self.end:
        #     raise StopIteration
        # temp = self.start
        # self.start += 1
        # return temp


for num in custom_range(1, 9):
    print(num)
