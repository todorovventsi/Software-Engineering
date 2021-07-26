class dictionary_iter:
    def __init__(self, collection):
        self.collection = collection
        self.keys = list(self.collection.keys())
        self.key_index = 0
        self.stop_at = len(self.keys) - 1

    def __iter__(self):
        return self

    def __next__(self):
        key_ind = self.key_index
        while self.key_index <= self.stop_at:
            key = self.keys[key_ind]
            self.key_index += 1
            return key, self.collection[key]
        raise StopIteration


result = dictionary_iter({1: "1", 2: "2"})

for x in result:
    print(x)
