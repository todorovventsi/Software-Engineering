class reverse_iter:
    def __init__(self, collection):
        self.collection = collection
        self.index = len(self.collection) - 1

    def __iter__(self):
        return self

    def __next__(self):
        while not self.index == -1:
            temp_i = self.index
            self.index -= 1
            return self.collection[temp_i]
        raise StopIteration


reversed_list = reverse_iter([1, 2, 3, 4])
for item in reversed_list:
    print(item)
