class vowels:
    def __init__(self, string):
        self.string = string
        self.end = len(string)
        self.start = 0
        self.vowels = "aeiouy"

    def __iter__(self):
        return self

    def __next__(self):
        while self.start < self.end:
            index = self.start
            if self.string[index].lower() in self.vowels:
                self.start += 1
                return self.string[index]
            self.start += 1
            continue
        raise StopIteration


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
