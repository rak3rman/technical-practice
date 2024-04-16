class Array(object):

    def __init__(self):
        self.array = []

    def __len__(self):
        return len(self.array)

    def __getitem__(self, index):
        return self.array[index]

    def __setitem__(self, index, value):
        self.array[index] = value

    def __delitem__(self, index):
        del self.array[index]

    def insert(self, index, value):
        self.array.insert(index, value)

    def append(self, value):
        self.array.append(value)

    def remove(self, value):
        self.array.remove(value)
