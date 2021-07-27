class sequence_repeat:
    def __init__(self, text, number):
        self.text = text
        self.number = number
        self.index = 0
        self.index_restart = len(text)
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter == self.number:
            raise StopIteration
        self.counter += 1
        if self.index == self.index_restart:
            self.index = 0
        value = self.text[self.index]
        self.index += 1
        return value


result = sequence_repeat('abc', 5)
for item in result:
    print(item, end ='')
